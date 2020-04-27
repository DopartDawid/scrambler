from bitarray import bitarray
import random


def scramble(array, scrambleKey):
    currentIndex = 0
    while(currentIndex < len(array)):
        print(array[currentIndex:(currentIndex+len(scrambleKey))])
        array[currentIndex:(currentIndex+len(scrambleKey))] = array[currentIndex:(currentIndex+len(scrambleKey))] ^ scrambleKey
        currentIndex += len(scrambleKey)
