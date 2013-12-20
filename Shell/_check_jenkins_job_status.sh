#! /bin/bash

# This script is to check the latest job status
# Calc function is included in another file, _convert_time_ms_s.sh

# This function is to get a job's status. With different status, output different content.
# Need one parameter.
Check_Job_Status()
{
	Job_Name=$1
	Out_File=/tmp/out_$(date +%H%M%S).json

	wget http://${MyJenkinsSite}/job/${Job_Name}/lastBuild/api/json -O ${Out_File} &>/dev/null
	[[ -e ${Out_File} ]] || (echo "No File Downloaded\!" && exit 100)

	tmp_date=$(cat ${Out_File} | tr "," "\n" | tr -d '"' | grep ^id | cut -d ":" -f 2 | head -n 1)
	for i in userId number result building duration
	do
		eval tmp_${i}=$(cat ${Out_File} | tr "," "\n" | tr -d '"' | grep $i: | cut -d ":" -f 2)
	done

	tmp_date_a=$(echo ${tmp_date} | cut -d "_" -f 1)
	tmp_date_b=$(echo ${tmp_date} | cut -d "_" -f 2 | tr "-" ":")
	tmp_date=$(date -d "${tmp_date_a} ${tmp_date_b} -0600")

	case ${tmp_building} in
	"true")
		tmp_building=Running
		;;
	"false")
		tmp_building=Complete
		;;
	*)
		tmp_building=T.T
		;;
	esac

	# Build Number
	if [[ "${tmp_building}" = "Complete" ]]
	then
		echo -e $'\e[34m'${Job_Name}'\e[m #'$'\e[1;37m'${tmp_number}'\e[m'
	else
		echo -e $'\e[34m'${Job_Name}'\e[m #'$'\e[1;37m'${tmp_number}'\e[m' $'\e[1;34m('${tmp_building}')\e[m'
		tmp_url=$(cat ${Out_File} | tr "," "\n" | tr -d '"' | grep url: | cut -d ":" -f 2,3)
		echo -e $'\t\e[7;36m'"${tmp_url}"'\e[m'
	fi

	# User + Date
	if [[ -n ${tmp_userId} ]]
	then
		echo -e $'\t\e[36mTriggered By\e[m'$'\e[32m'" ${tmp_userId}"'\e[m'
	fi
	echo -e $'\t\e[36mTriggered On\e[m'$'\e[32m'" ${tmp_date}"'\e[m'
	
	# Result
	if [[ "${tmp_building}" = "Complete" ]]
	then
		case ${tmp_result} in
			"SUCCESS")
				echo -e '\t\e[36mResult:\e[m''\e[32m'" ${tmp_result}"'\e[m'
				Calc ${tmp_duration}
				;;
			"FAILURE")
				echo -e '\t\e[36mResult:\e[m''\e[1;31m'" ${tmp_result}"'\e[m'
				tmp_url=$(cat ${Out_File} | tr "," "\n" | tr -d '"' | grep url: | cut -d ":" -f 2,3)
				echo -e '\t\e[36mURL: \e[m''\e[7;31m'"${tmp_url}"'\e[m'
				Calc ${tmp_duration}
				;;
			"UNSTABLE")
				echo -e '\t\e[36mResult:\e[m''\e[1;33m'" ${tmp_result}"'\e[m'
				tmp_url=$(cat ${Out_File} | tr "," "\n" | tr -d '"' | grep url: | cut -d ":" -f 2,3)
				echo -e '\t\e[36mURL:\e[m''\e[7;33m'" ${tmp_url}"'\e[m'
				Calc ${tmp_duration}
				;;
			*)
				echo -e '\t\e[36mResult:\e[m''\e[37m'" ${tmp_result}"'\e[m'
				Calc ${tmp_duration}
				;;
		esac
	fi
	rm ${Out_File}
}

reset
JobList=/tmp/filelist
MyJenkinsSite=http://localhost

# job list
cat >${JobList} <<-JobList
		HELLO_WORLD
JobList

cat ${JobList} | while read job
do
	Check_Job_Status $job
done
