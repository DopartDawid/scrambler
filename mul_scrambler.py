from bitarray import bitarray
# POLYNOMIAL (1 + z^(-4) + z^(-9))

POLYNOMIAL_INDEX1 = 5
POLYNOMIAL_INDEX2 = 10

def MULScramble(array):
    currentIndex = POLYNOMIAL_INDEX2
    while(currentIndex < array.length()):
        array[currentIndex] = array[currentIndex] ^ (array[currentIndex-POLYNOMIAL_INDEX1] ^ array[currentIndex-POLYNOMIAL_INDEX2])
        currentIndex += 1

def MULDescramble(array):
    currentIndex = POLYNOMIAL_INDEX2
    oldArray = array.copy()
    while(currentIndex < oldArray.length()):
        array[currentIndex] = oldArray[currentIndex] ^ (oldArray[currentIndex-POLYNOMIAL_INDEX1] ^ oldArray[currentIndex-POLYNOMIAL_INDEX2])
        currentIndex += 1
    return array