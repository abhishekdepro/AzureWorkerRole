#!/bin/bash

# This script opens 4 terminal windows.

now=0
count=0
echo $now
i=12
p=$now
while true
do
now=$(date +"%M")
if [ $(( $now % 100  )) -eq "0" ]; then
count=1
	if [ $count -eq "0" ]; then
		python /home/abhishek/AzureWorkerRole/AzureTableStore.py
	fi
fi
done
