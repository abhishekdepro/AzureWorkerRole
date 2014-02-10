#!/bin/bash

# This script opens 4 terminal windows.

now=0

echo $now
i=12
p=$now
while true
do
now=$(date +"%M")
if [ $(( $now % 10  )) -eq "0" ]; then
    python AzureTableStore.py
fi
done
