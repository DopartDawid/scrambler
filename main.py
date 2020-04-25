from bitarray import bitarray
import random

procentJedynek = random.randint(0,100)
print(procentJedynek)

mainData = bitarray(1000)
mainData.setall(False)

# procentJedynek * 10, to jest procentJedynek/100 * liczba_bitów
count = 0
while(count < procentJedynek * 10):
    miejsceNaJedynke = random.randint(0, 999)
    if mainData[miejsceNaJedynke] == False:
        mainData[miejsceNaJedynke] = True
        #mainData.reverse();
        #mainData.set(True, [miejsceNaJedynke])
        count = count + 1


print(mainData)
