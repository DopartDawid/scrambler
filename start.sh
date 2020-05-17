#!/bin/bash
# used: bash start.sh FILE_NAME MEASUREMENTS PERCENTAGE
FILE_NAME=$1
MEASUREMENTS=$2
PERCENTAGE=$3

echo "$MEASUREMENTS,$PERCENTAGE" > $FILE_NAME

for((value=1;value<=MEASUREMENTS;value++))
do
    python3 main.py $FILE_NAME $PERCENTAGE
    echo "Generated: $value"
done
    echo "CSV output generated"