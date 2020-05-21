from bitarray import bitarray
import random
import csv
import sys
from xor_scrambler import XORScramble, XORShiftKeyGenerator
from mul_scrambler import MULScramble, MULDescramble
from negationScrambler import negationScramble

PACKET_LENGTH = 8
BIT_ARRAY_LENGTH = int(sys.argv[3])*8
SCRAMBLE_SEED = 0X27  # Key's length should be a divider of bitarray length.
PERCENTAGE_OF_ONES = int(sys.argv[2])


def initArray(array):
    # Get a random number, between 0 and 100.
    # This number is the percentage of "1's" in out array.
    # percentageOfOnes = random.randint(0, 100)
    percentageOfOnes = PERCENTAGE_OF_ONES
    # print("Procent: ", percentageOfOnes)

    # Initially we set our array to contain only "0's".
    array.setall(False)

    # This loop's purpose is to allocate the "1's" in a random manner.
    iterationVar = ((array.length() * percentageOfOnes) / 100)
    while(iterationVar > 0):
        indexForOne = random.randint(0, array.length() - 1)
        if array[indexForOne] is False:
            array[indexForOne] = True
            iterationVar = iterationVar - 1


# Shows stats of a bitarray
def getStats(array, statsArray):
    currentIndex = 1
    currentSeq = 1
    # Counting every occurence
    while(currentIndex < len(array)):
        if array[currentIndex] is array[currentIndex-1]:
            currentSeq += 1
        else:  # If next is not the same, we save count current sequence
            statsArray[currentSeq] += 1
            currentSeq = 1

        currentIndex += 1
    statsArray[currentSeq] += 1     # Adding last sequence

    index = 2
    while(index < len(statsArray)):
        statsArray[0] += statsArray[index] * 2.5**(index-3)
        index += 1


def main():

    mainData = bitarray(BIT_ARRAY_LENGTH)
    initArray(mainData)
    mainDataMUL = mainData.copy()
    mainDataNEGATE = mainData.copy()

    with open('mainData_file', 'w', newline = '') as mainData_file:
        writer = csv.writer(mainData_file, delimiter = ',')
        writer.writerow(mainData)


    # DEBUG
    # print(mainData)

    mainStats = []
    for num in range(0, PACKET_LENGTH + 1):
        mainStats.append(0)

    # Getting stats
    packetIndex = 0
    while(packetIndex < mainData.length()):
        statsArray = []
        for num in range(0, PACKET_LENGTH + 1):
            statsArray.append(0)

        getStats(mainData[packetIndex:packetIndex+PACKET_LENGTH-1], statsArray)
        packetIndex += PACKET_LENGTH
        if statsArray[0] > random.uniform(0, 100):
            mainStats[0] += 1

        index = 1
        while(index < len(statsArray)):
            mainStats[index] += statsArray[index]
            index += 1
    '''
    # Showing stats (0 and 1 is not important)
    currentIndex = 2
    while (currentIndex < len(mainStats)):
        if mainStats[currentIndex] != 0:
            print(currentIndex, " powtorzylo sie: ", mainStats[currentIndex])
        currentIndex += 1
    print("Zepsute pakiety: ", mainStats[0])
    '''
    with open(sys.argv[1] + '_BeforeScramble','a', newline='') as outputfile:
        writer = csv.writer(outputfile, delimiter = ',')
        writer.writerow(mainStats)

    #print('\n\n\n\n')   # SCRAMBLING HERE

    XORScramble(mainData, XORShiftKeyGenerator(SCRAMBLE_SEED))
    MULScramble(mainDataMUL)
    negationScramble(mainDataNEGATE)

    # print(mainData)

    mainStats = []
    for num in range(0, PACKET_LENGTH + 1):
        mainStats.append(0)

    # Getting stats
    packetIndex = 0
    while(packetIndex < mainData.length()):
        statsArray = []
        for num in range(0, PACKET_LENGTH + 1):
            statsArray.append(0)

        getStats(mainData[packetIndex:packetIndex+PACKET_LENGTH-1], statsArray)
        packetIndex += PACKET_LENGTH
        if statsArray[0] > random.uniform(0, 100):
            mainStats[0] += 1

        index = 1
        while(index < len(statsArray)):
            mainStats[index] += statsArray[index]
            index += 1

    with open(sys.argv[1] + "_XOR",'a', newline='') as outputfile:
        writer = csv.writer(outputfile, delimiter = ',')
        writer.writerow(mainStats)

    # MAIN STATS FOR MUL SCRAMBLE
    mainStats= []
    for num in range(0, PACKET_LENGTH + 1):
        mainStats.append(0)

    # Getting stats
    packetIndex = 0
    while(packetIndex < mainDataMUL.length()):
        statsArray = []
        for num in range(0, PACKET_LENGTH + 1):
            statsArray.append(0)

        getStats(mainDataMUL[packetIndex:packetIndex+PACKET_LENGTH-1], statsArray)
        packetIndex += PACKET_LENGTH
        if statsArray[0] > random.uniform(0, 100):
            mainStats[0] += 1

        index = 1
        while(index < len(statsArray)):
            mainStats[index] += statsArray[index]
            index += 1

    with open(sys.argv[1] + "_MUL",'a', newline='') as outputfile:
        writer = csv.writer(outputfile, delimiter = ',')
        writer.writerow(mainStats)

    # MAIN STATS FROM NEGATE SCRAMBLER
    mainStats = []
    for num in range(0, PACKET_LENGTH + 1):
        mainStats.append(0)

    # Getting stats
    packetIndex = 0
    while(packetIndex < mainDataNEGATE.length()):
        statsArray = []
        for num in range(0, PACKET_LENGTH + 1):
            statsArray.append(0)

        getStats(mainDataNEGATE[packetIndex:packetIndex+PACKET_LENGTH-1], statsArray)
        packetIndex += PACKET_LENGTH
        if statsArray[0] > random.uniform(0, 100):
            mainStats[0] += 1

        index = 1
        while(index < len(statsArray)):
            mainStats[index] += statsArray[index]
            index += 1

    with open(sys.argv[1] + "_NOT",'a', newline='') as outputfile:
        writer = csv.writer(outputfile, delimiter = ',')
        writer.writerow(mainStats)
    '''
    # Showing stats (0 and 1 is not important)
    currentIndex = 2
    while(currentIndex < len(mainStats)):
        if mainStats[currentIndex] != 0:
            print(currentIndex, " powtorzylo sie: ", mainStats[currentIndex])
        currentIndex += 1
    print("Zepsute pakiety: ", mainStats[0])
    '''








if __name__ == "__main__":
    main()
