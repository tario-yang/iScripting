#! /bin/bash

# This script is to calculate the resources used by one or more than one PIDs
# Resource: CPU + Memory



# v1.0
#	Create first version
#	Current work flow:
#		1. Splite a *top collection file* to multiple files.
#		2. From each sub file,
#			a. Fetch CPU and Memory state of whole operation system.
#			b. Fetch pointed process's CPU and Memory state.
#			c. Fetch process id and number of processes (in comment field)
# v1.1
#	Support process list
#	Update help content
#	Refine variables' name



# Precondition
clear

## Help
if [[ "$1" = "--help" ]] || [[ -z $1 ]]
then
	cat <<HELP

Usage:
	${0##*/} -f [Top Collection File] -p [Process Name1,Process Name2,...  The default value is *postgres:*]
	${0##*/} [--help]

HELP

	exit 0
fi

cat <<PRECONDITION

It is necessary to use the following configuration content for TOP, creating/replacing ".toprc" under your HOME Directory,
 
RCfile for "top with windows"		# shameless braggin'
Id:a, Mode_altscr=0, Mode_irixps=1, Delay_time=3.000, Curwin=1
Def	fieldscur=AEHIOQTWKNMbcdfgjplrsuvyzX
	winflags=64825, sortindx=10, maxtasks=0
	summclr=1, msgsclr=1, headclr=3, taskclr=1
Job	fieldscur=ABcefgjlrstuvyzMKNHIWOPQDX
	winflags=65465, sortindx=10, maxtasks=0
	summclr=6, msgsclr=6, headclr=7, taskclr=6
Mem	fieldscur=ANOPQRSTUVbcdefgjlmyzWHIKX
	winflags=62777, sortindx=13, maxtasks=0
	summclr=5, msgsclr=5, headclr=4, taskclr=5
#Usr	fieldscur=ABDECGfhijlopqrstuvyzMKNWX
	winflags=62777, sortindx=4, maxtasks=0
	summclr=3, msgsclr=3, headclr=2, taskclr=3


Before running your testing, start to execute following command line,
	top -b -n [Num] | tee [Output File]
This command will generate a *top collection file*. And the generated file will be used by this script.

PRECONDITION

echo;echo;echo;echo;echo;

# Function: Splite the TOP collection
function SpliteFile()
{
	# Parameter
	SpliteFile_Number=/tmp/$(date +%F%H%M%S)

	# Start to splite
	echo "Start to split,"
	cat "$1" | while read m
	do
		if [[ `echo $m | grep "^top"` ]]
		then
			SpliteFile_OperateOutput="$2/$(date +%H%M%S)"
			echo "$m" >> ${SpliteFile_OperateOutput}
			printf . | tee -a ${SpliteFile_Number}
			sleep 1
		else
			echo "$m" >> ${SpliteFile_OperateOutput}
		fi
	done
	echo
}

# Get *Total* CPU and Memory state
function TotalCPUMEMState()
{
	# CPU
	TotalCPUMEMState_TotalCPU=$(grep ^Cpu $1 | awk '{print $2$3}' | tr -d "usy")

	# Mem
	TotalCPUMEMState_TotalMem=$(grep ^Mem $1 | awk '{print $2,$4,$6,$8}' | tr " " ",") 

	# Swap
	TotalCPUMEMState_TotalSwap=$(grep ^Swap $1 | awk '{print $2,$4,$6,$8}' | tr " " ",") 

	#Output
	echo -n "${TotalCPUMEMState_TotalCPU}${TotalCPUMEMState_TotalMem},${TotalCPUMEMState_TotalSwap}" >>$2
}

# Get *pointed* Processes' CPU and Memory
function CPUMEMState()
{
	# Start to check
	## Total
	TotalCPUMEMState $1 $2

	## State of pointed process name
	CPUMEMState_Output=""
	for k in ${ProcessName}
	do
		CPUMEMState_CPU=""
		CPUMEMState_Mem=""
		CPUMEMState_Comment=""
		CPUMEMState_LIST=$(grep $k $1)
			if [[ -z ${CPUMEMState_LIST} ]]
			then
				echo "Fail to find \"$k\"".
				for ((z=0;z<${CSV_Header_Count};z++))
				do
					printf , >>$2
				done
				echo >>$2
				continue
			else
				CPUMEMState_CPU=$(echo "${CPUMEMState_LIST}" | awk '{SUM+=$4} END {print SUM}')
				CPUMEMState_Mem=$(echo "${CPUMEMState_LIST}" | awk '{SUM+=$5} END {print SUM}')
				CPUMEMState_Comment=$(echo "${CPUMEMState_LIST}" | awk '{print $1}' | tr "\n" "+")END
			fi
			CPUMEMState_Output=${CPUMEMState_Output},\"${CPUMEMState_CPU}\",\"${CPUMEMState_Mem}\",\"${CPUMEMState_Comment}\"
	done
	#Output
	echo ${CPUMEMState_Output} >>$2
}


# Define Parameters


parameter1=$(echo "$*" | cut -d "-" -f 2)
parameter2=$(echo "$*" | cut -d "-" -f 3)

echo $parameter2

# Initiate Parameters
for i in "${parameter1}" "${parameter2}"
do
	case ${i:0:1} in
		"f")
			TOPFile=${i:2}
			;;
		"p")
			ProcessName=$(echo ${i:2} | tr "," " ")
			;;
	esac
done

if [[ -z ${TOPFile} ]]
then
	echo "TOP Collection File is NOT defined!";echo;echo;echo
	exit 1
fi

if [[ -z ${ProcessName} ]]
then
	ProcessName="postgres:"
fi

# Check Parameters
## Check whether input file is valid
if [[ `grep "^top" ${TOPFile}` ]]
then
        echo "Valid Input File!"
else
        echo "Invalid Input File!"
        sleep 1
        exit 1
fi
## Check and generate CSV header according to process list
CSV_Header='"ID","CPU User","CPU System","Mem Total","Mem Used","Mem Free","Mem Buffers","Swap Total","Swap Used","Swap Free","Swap Cached"'
for i in ${ProcessName}
do
	CSV_Header="${CSV_Header}"',"%CPU '$i'","%Mem '$i'","Comment"'
done
CSV_Header_Count=$(echo "${CSV_Header}" | awk -F "," '{print NF}')
CSV_Header_Count=$((${CSV_Header_Count}-11))

### Split file
tmpDIR=/tmp/$(date +%Y%m%d%H%M%S)
echo "Workspace is ${tmpDIR}"
test -e ${tmpDIR} || mkdir $_
SpliteFile ${TOPFile} ${tmpDIR}

### Create Array
FileList=($(ls -tr ${tmpDIR}))

### Check each file
echo "Start to generate data..."
OutputFile="Output_$(date +%Y%m%d%H%M%S).csv"
	echo "Report: ${OutputFile}"
	echo "Header:"
	echo $'\t'${CSV_Header}
	echo ${CSV_Header} >${OutputFile}
	for ((j=0;j<${#FileList[*]};j++))
	do
		echo -n "$j," >>${OutputFile}
		CPUMEMState ${tmpDIR}/${FileList[$j]} ${OutputFile}
		echo [job \#$j] Over
	done

echo "Over."
