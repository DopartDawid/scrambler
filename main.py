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
        count = count + 1

print(mainData)

# scrambling here

count3 = 0
counter = 0
for num in range(1,999):
    if mainData[num-1] != mainData[num]:
        counter = 0
    else:
        counter = counter + 1
    if counter == 2:
        counter = -1
        count3 = count3 + 1
print(count3)





