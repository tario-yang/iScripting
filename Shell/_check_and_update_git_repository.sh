#! /bin/bash
# This script is to check and update the selected Git Repository.

## Operation: Git Pull
function UpdateLocalRepository()
{
        echo -n -e '\e[36mCheck local repository...\e[m'
        Git_Status=$(git status -s)
        [[ -n ${Git_Status} ]] && echo -e '\e[1;31mDetected local change(s). Please pay attention...\e[m' || echo -e '\e[33mOK!\e[m'
        echo -e '\e[36mStart to update local repository...\e[m'
        [[ `git pull origin master` ]] && echo -e '\e[1;33mStatus: Updated!\e[m' || echo -e '\e[1;31mStatus: Failed!\e[m'
}

## Operation: Check whether local and remote sides are same.
function CheckLocalGitRepository()
{
        ## Display Git Version
        clear
        echo -e '\e[1;31m******************************\e[m'
        echo -e '\e[1;31m'   $(git --version)'\e[m'
        echo -e '\e[1;31m******************************\e[m'
        echo;

        ## Define the variables
        GITDIR=/Your/Directory/To/Save/Git/Repository ### This directory shall exist.
        DEFAULT_REPO="Default Git Repo" ### When there is no input got, script chooses the default value.
        RECORD='.tmp_GitRepoList' ### Use this temporary to save list got.
        cat /dev/null 1>${RECORD}

        ## List current Git Repository under $GITDIR
        echo -e '\e[1;37m'"Current Git Repository list (under $GITDIR):"'\e[m'
        i=0; ls -l ${GITDIR} | grep ^d | awk '{print $NF}' | while read line
        do
                ((i++))
                echo "${i}: $line" | tee -a ${RECORD} ### Save the line to temporary file as well.
        done

        ## Ask Input
        echo;echo -n -e '\e[32mPlease select one repository: \e[m'
        read RL
        [[ -z $RL ]] && RL=$(grep ${DEFAULT_REPO} ${RECORD} | cut -d ":" -f 1) ### Set a default value when there is no input
        [[ -z $RL ]] && exit 1 ### Exit when previous 'set default value' step fails.
        GIT_HOME=$(grep ^${RL} ${RECORD} | cut -d " " -f 2) ### Get the Repository name from temporary file.
        echo;echo -e '\e[36m'"Selected ${GIT_HOME}"'\e[m'

        ## Enter the directory of Repository
        cd ${GITDIR}/${GIT_HOME}

        ## Compare whether local and remote HEAD are same
        Local_HashID=$(git rev-parse HEAD)
        Remote_Repo_URL=$(git remote -v | awk '/fetch/{print $2}')
        Remote_HashID=$(git ls-remote ${Remote_Repo_URL} master | awk '{print $1}')
        [ ${Local_HashID} != "" -a ${Local_HashID} = ${Remote_HashID} ] && echo -e '\e[1;33mStatus: Already up-to-date!\e[m' || UpdateLocalRepository
        echo
}

CheckLocalGitRepository
