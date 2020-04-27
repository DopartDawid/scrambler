from bitarray import bitarray
# POLYNOMIAL (1 + z^(-4) + z^(-9))

POLYNOMIAL_INDEX1 = 10
POLYNOMIAL_INDEX2 = 40

def MULScramble(array):
    currentIndex = POLYNOMIAL_INDEX1
    while(currentIndex < array.length()):
        array[currentIndex] = array[currentIndex] ^ (array[currentIndex-POLYNOMIAL_INDEX1] ^ array[currentIndex-POLYNOMIAL_INDEX2])
        currentIndex += 1

def MULDescramble(array):
    currentIndex = POLYNOMIAL_INDEX1
    oldArray = array.copy()
    array = bitarray(old)
    while(currentIndex < array.length()):
        array[currentIndex] = array[currentIndex] ^ (array[currentIndex-POLYNOMIAL_INDEX1] ^ array[currentIndex-POLYNOMIAL_INDEX2])
        currentIndex += 1
    return array