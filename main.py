from bitarray import bitarray
import random
from xor_scrambler import XORScramble

BIT_ARRAY_LENGTH = 100
PACKET_LENGTH = 100
SCRAMBLE_KEY = bitarray('1110011011') # Key's length should be a divider of bitarray length.


def initArray(array):
    # Get a random number, between 0 and 100.
    # This number is the percentage of "1's" in out array.
    percentageOfOnes = random.randint(0, 100)

    # DEBUG!!!!!!
    print("Procent: ", percentageOfOnes)

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


def main():
    mainData = bitarray(BIT_ARRAY_LENGTH)
    initArray(mainData)
    # DEBUG
    print(mainData)

    # Initializing array with stats
    statsArray = []
    for num in range(0, PACKET_LENGTH + 1):
        statsArray.append(0)

    getStats(mainData, statsArray)

    # Showing stats (0 and 1 is not important)
    currentIndex = 2
    while(currentIndex < len(statsArray)):
        if statsArray[currentIndex] != 0:
            print(currentIndex, " powtorzylo sie: ", statsArray[currentIndex])
        currentIndex += 1

    print('\n\n\n\n') # SCRAMBLING HERE

    XORScramble(mainData, SCRAMBLE_KEY)
    print(mainData)
    statsArray = []
    for num in range(0, PACKET_LENGTH + 1):
        statsArray.append(0)

    getStats(mainData, statsArray)

    # Showing stats (0 and 1 is not important)
    currentIndex = 2
    while(currentIndex < len(statsArray)):
        if statsArray[currentIndex] != 0:
            print(currentIndex, " powtorzylo sie: ", statsArray[currentIndex])
        currentIndex += 1

if __name__ == "__main__":
    main()
