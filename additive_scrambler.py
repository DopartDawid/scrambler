from bitarray import bitarray
import random

# Define the scramblingArray variable, but wait with
# the initalization.
scramblingArray = None


def scramble(array, percentageOfOnes):
    scramblingArray = bitarray(len(array))
    scramblingArray.setall(False)

    # Scrambling array initalization
    # Maybe use initArray from main.py?
    iterationVar = ((array.length() * percentageOfOnes) / 100)

    while(iterationVar > 0):
        indexForOne = random.randint(0, array.length() - 1)
        if array[indexForOne] is False:
            array[indexForOne] = True
            iterationVar = iterationVar - 1

    # Actual scrambling
    index = 0
    while(index < len(array)):
        array[index] = array[index] ^ scramblingArray[index]


def descramble(array):
    index = 0
    while(index < len(array)):
        array[index] = array[index] ^ scramblingArray[index]
