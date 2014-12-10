clear
alias l='ls -lh --color'
alias la='ls -alh --color'
alias REPO='. ~/.bashrc'

# Preparation Check for GIT
function UpdateLocalRepository()
{
        echo -n -e '\e[36mCheck local repository...\e[m'
        Git_Status=$(git status -s)
        [[ -n ${Git_Status} ]] && echo -e '\e[1;31mDetected local change(s). Please pay attention...\e[m' || echo -e '\e[33mOK!\e[m'
        echo -e '\e[36mStart to update local repository...\e[m'
        [[ `git pull origin master` ]] && echo -e '\e[1;33mStatus: Updated!\e[m' || echo -e '\e[1;31mStatus: Failed!\e[m'
}

function CheckLocalGitRepository()
{
	# Preparation Check for GIT
	echo -e '\e[1;31m******************************\e[m'
	echo -e '\e[1;31m'   $(git --version)'\e[m'
	echo -e '\e[1;31m******************************\e[m'
	echo;
	GITDIR=/d/iWS
	RECORD='.tmp_GitRepoList'
	cat /dev/null 1>${RECORD}
	i=0
	echo -e '\e[1;37m'"Current Git Repository list (under $GITDIR):"'\e[m'
	ls -l ${GITDIR} | grep ^d | awk '{print $NF}' | while read line
	do
		((i++))
		echo "${i}: $line" | tee -a ${RECORD}
	done
	echo;echo -n -e '\e[32mPlease select one repository: \e[m'
	read RL
	[[ -z $RL ]] && RL=$(grep 'HW_Document' ${RECORD} | cut -d ":" -f 1)
	[[ -z $RL ]] && exit 1
	RL=${RL}":"
	GIT_HOME=$(grep ^${RL} ${RECORD} | cut -d " " -f 2)
	echo;echo -e '\e[36m'"Selected ${GIT_HOME}"'\e[m'
	rm ${RECORD}
	cd ${GITDIR}/${GIT_HOME}
	Local_HashID=$(git rev-parse HEAD)
	Remote_Repo_URL=$(git remote -v | awk '/fetch/{print $2}')
	Remote_HashID=$(git ls-remote ${Remote_Repo_URL} master | awk '{print $1}')
	[ ${Local_HashID} != "" -a ${Local_HashID} = ${Remote_HashID} ] && echo -e '\e[1;33mStatus: Already up-to-date!\e[m' || UpdateLocalRepository
	echo
}

CheckLocalGitRepository
