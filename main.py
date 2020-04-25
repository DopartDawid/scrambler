from bitarray import bitarray
import random

BIT_ARRAY_LENGTH = 1000

# Get a random number, between 0 and 100.
# This number is the percentage of "1's" in out array.
percentageOfOnes = random.randint(0,100)
print(percentageOfOnes)

mainData = bitarray(BIT_ARRAY_LENGTH)
# Initially we set our array to contain only "0's".
mainData.setall(False)

# This loop's purpose is to allocate the "1's" in a random manner.
iterationVar = ((mainData.length() * percentageOfOnes) / 100 )
while(iterationVar > 0):
    indexForOne = random.randint(0, mainData.length() - 1)
    if mainData[indexForOne] == False:
        mainData[indexForOne] = True
        iterationVar = iterationVar - 1

print(mainData)

# scrambling here

count3 = 0
counter = 0
#for num in range(1,999):


print(count3)

'''
if mainData[num-1] != mainData[num]:
    counter = 0
else:
    counter = counter + 1
if counter == 2:
    counter = -1
    count3 = count3 + 1'''
