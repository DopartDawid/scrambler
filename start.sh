#!/bin/bash
# used: bash start.sh FILE_NAME MEASUREMENTS PERCENTAGE PACKETS_SENT
FILE_NAME=$1
MEASUREMENTS=$2
PERCENTAGE=$3
PACKETS_SENT=$4

rm -f -r xor_output
rm -f -r mul_output
rm -f -r not_output
rm -f -r before_output
rm -f "${FILE_NAME}_XOR"
rm -f "${FILE_NAME}_BeforeScramble"
rm -f "${FILE_NAME}_NOT"
rm -f "${FILE_NAME}_MUL"

echo "$MEASUREMENTS, $PERCENTAGE, $PACKETS_SENT" >> "${FILE_NAME}_BeforeScramble"
echo "$MEASUREMENTS, $PERCENTAGE, $PACKETS_SENT" >> "${FILE_NAME}_XOR"
echo "$MEASUREMENTS, $PERCENTAGE, $PACKETS_SENT" >> "${FILE_NAME}_NOT"
echo "$MEASUREMENTS, $PERCENTAGE, $PACKETS_SENT" >> "${FILE_NAME}_MUL"

for((value=1;value<=MEASUREMENTS;value++))
do
    python3 main.py $FILE_NAME $PERCENTAGE $PACKETS_SENT &
    echo "Generated: $value"
done
    echo "CSV output generated"

mkdir before_output
mkdir xor_output
mkdir mul_output
mkdir not_output

python3 statsgen.py "${FILE_NAME}_BeforeScramble" before_output/stats_before
python3 statsgen.py "${FILE_NAME}_XOR" xor_output/stats_xor
python3 statsgen.py "${FILE_NAME}_MUL" mul_output/stats_mul
python3 statsgen.py "${FILE_NAME}_NOT" not_output/stats_not