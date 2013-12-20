#! /bin/bash

# This function is to check the duration of a job. Based on current duration of each jenkins jobs, it is not necessary to calculate the Day unit.
# Output format is H:M:S

function Calc() 
{
        
    H=0
	M=0
	S=0

	DUR=$(($1/1000)) 

	if [[ ${DUR} -eq 0 ]]
	then    
		return
	fi
	   
	while :
	do
		if [[ $(expr $DUR - 3600) -ge 0 ]]
		then
			((H++))
			DUR=$((DUR-3600))
		else
			break
		fi
	done
	   
	while :
	do
		if [[ $(expr $DUR - 60) -ge 0 ]]
		then
			((M++))
			DUR=$((DUR-60))
		else
			S=$DUR
			break
		fi
	done
	echo -e '\t\e[36mDuration: \e[m''\e[1;34m'$H:$M:$S'\e[m'
}
