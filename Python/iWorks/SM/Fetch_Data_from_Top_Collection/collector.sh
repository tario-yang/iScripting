OUT="Java_Native_Memory_Recorder.log"
while [[ -n $(ps -ef | grep ${JMeterPath} | grep -v grep | awk '{print $2}') ]]
do
    cf ssh ${TENANT}_max -c "date +%Y%m%d_%H%M%S%z_%N" >> ${OUT}
    echo >> ${OUT}
    cf app ${TENANT}_max > tmp.app.stat
        maxline=$(cat tmp.app.stat | wc -l)
        sed -n $(expr ${maxline} - 1),${maxline}p >> ${OUT}
    cf ssh ${TENANT}_max -c "top -b -n 3 " >> ${OUT}
    cf ssh ${TENANT}_max -c "top -b -n 3 -p ${P1},${P2}" >> ${OUT}
    cf ssh ${TENANT}_max -c "/home/vcap/app/.java-buildpack/open_jdk_jre/bin/jcmd ${jProc} VM.native_memory summary" >> ${OUT}
    echo >> ${OUT} 
    sleep 2
done
