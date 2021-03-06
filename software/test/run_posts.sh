#!/bin/bash

if [ "$#" -lt 2 ]
then
    echo "`basename $0`: usage: $0 host port"
    exit 1
fi

HOST=$1
PORT=$2
INTERVAL=0
DELAY=0
TOTAL_DELAY=0

# set random range delay (0 to this # in ms)
MAX_DELAY=50

SENSOR_DATA=sensor_records.out

OLD_IFS=${IFS}
IFS=$'\n'

MSGS=(
`cat ${SENSOR_DATA}`
)

IFS=${OLD_IFS}

MSG_COUNT=${#MSGS[@]}

echo `basename $0`: $MSG_COUNT messages to be sent to ${HOST}:${PORT} via UDP
echo
echo "--------------------------------------------------------------"

START_DATE_TIME=`date`

START_TIME=`date +%s`

for (( i=0; i <${MSG_COUNT}; i++ ));
do
    echo -n "Sending MSGS[${i}]: \"${MSGS[$i]}\"..."
    echo -n "${MSGS[$i]}" > /dev/udp/$HOST/$PORT
    echo "  sent."

    DELAY=`printf %03d $((RANDOM % ${MAX_DELAY}))`
    TOTAL_DELAY=`expr ${TOTAL_DELAY} + ${DELAY}`
    echo "Delaying for 0.${DELAY}s ..."
    sleep "0.${DELAY}"
done

END_TIME=`date +%s`

TOTAL_DELAY_CHAR_LEN=`echo -n ${TOTAL_DELAY} | wc -c`
TOTAL_DELAY_MSECS_OFFSET=`expr ${TOTAL_DELAY_CHAR_LEN} - 2`
TOTAL_DELAY_SECS=`expr ${TOTAL_DELAY} / 1000`
TOTAL_DELAY_SUBSECS=`echo ${TOTAL_DELAY} | cut -c ${TOTAL_DELAY_MSECS_OFFSET}-`

echo "--------------------------------------------------------------"
echo
echo "Started @ ${START_DATE_TIME}"
echo
echo "Finished @ `date`"
echo
echo "Elapsed time for this test was `expr \( ${END_TIME} - ${START_TIME} \) / 60` min `expr \( ${END_TIME} - ${START_TIME} \) % 60` sec"
echo
echo "Total inter-packet delays were ${TOTAL_DELAY_SECS}.${TOTAL_DELAY_SUBSECS}secs using a max inter-packet delay of ${MAX_DELAY}ms"
