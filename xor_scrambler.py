
def XORScramble(array, scrambleKey):
    currentIndex = 0
    while(currentIndex < len(array)):
        array[currentIndex:(currentIndex+len(scrambleKey))] = array[currentIndex:(currentIndex+len(scrambleKey))] ^ scrambleKey
        currentIndex += len(scrambleKey)
