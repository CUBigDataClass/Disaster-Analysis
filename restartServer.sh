#!/bin/sh

previousProcessId=`echo $(cat /home/ec2-user/Disaster-Analysis/.processID) `

echo $previousProcessId

if [[ $previousProcessId == "" ]]; then
	source /home/ec2-user/Disaster-Analysis/venv/bin/activate
	python /home/ec2-user/Disaster-Analysis/storeTweetsInMongoDBUsingTweepy.py &
	echo "$!"  > /home/ec2-user/Disaster-Analysis/.processID
elif [[ $previousProcessId != "" ]]; then
	checkProcessID=`echo $(ps -ef | egrep -iw $previousProcessId | grep -iv "grep" | wc -l )`
	if [[ $checkProcessID == 0 ]]; then
		source /home/ec2-user/Disaster-Analysis/venv/bin/activate
		python /home/ec2-user/Disaster-Analysis/storeTweetsInMongoDBUsingTweepy.py &
		echo "$!"  > /home/ec2-user/Disaster-Analysis/.processID
	fi
	#echo $checkProcessID
fi
#source /home/ec2-user/Disaster-Analysis/venv/bin/activate
#python /home/ec2-user/Disaster-Analysis/storeTweetsInMongoDBUsingTweepy.py &
#echo "$!"  > /home/ec2-user/Disaster-Analysis/.processID
