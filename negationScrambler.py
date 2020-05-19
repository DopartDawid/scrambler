from bitarray import bitarray

def negationScramble(array):
    currentIndex = 0
    while(currentIndex < array.length()):
        ~array[currentIndex]
        currentIndex += 2

