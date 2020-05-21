from bitarray import bitarray
from bitarray.util import int2ba


def XORScramble(array, scrambleKey):
    currentIndex = 0
    while(currentIndex < len(array)):
        array[currentIndex:(currentIndex+len(scrambleKey))] = array[currentIndex:(currentIndex+len(scrambleKey))] ^ scrambleKey
        currentIndex += len(scrambleKey)


# Polynomial 1+z^(-3)+z^(4)+z^(-7)
def XORShiftKeyGenerator(seed):
    generatedKey = seed

    generatedKey ^= generatedKey >> 3
    generatedKey ^= generatedKey << 2
    generatedKey ^= generatedKey >> 7
    # print(int2ba(generatedKey))
    return int2ba(generatedKey)


def XORKeyGenerator(seed):
    generatedKey = seed

    generatedKey ^= generatedKey >> 3
    generatedKey ^= generatedKey << 2
    generatedKey ^= generatedKey >> 7
    # print(int2ba(generatedKey))
    return int2ba(generatedKey)
