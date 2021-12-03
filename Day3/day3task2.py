filePath = 'input.txt'
file = open(filePath, 'r')
lines = file.readlines()
gammaRate = ''
epsilonRate = ''
positiveBitCounterList = []
isInitialized = False
lengthOfLine = 0
linesCounter = 0
oxygenGeneratorRating = 0
co2scrubberRating = 0
listForOxygen = []
listForCo2 = []
positiveBitCounter = 0
mostCommonFirstBitValue = ''
currentBitIndex = 0

# check most common and less common
for line in lines:
    if(line[0] == '1'):
        positiveBitCounter += 1
    linesCounter += 1

if(positiveBitCounter > linesCounter/2):
    mostCommonFirstBitValue = '1'
else:
    mostCommonFirstBitValue = '0'

# build both lists
for line in lines:
    if(line[0] == mostCommonFirstBitValue):
        listForOxygen.append(line.strip())
        continue
    listForCo2.append(line.strip())

positiveBitCounter = 0
mostCommonBit = ''
currentLenOfListForOxygenList = len(listForOxygen)
currentBitIndex = 1

# oxygen
while(currentLenOfListForOxygenList > 1):
    for number in listForOxygen:
        if(number[currentBitIndex] == '1'):
            positiveBitCounter += 1
    if(positiveBitCounter >= currentLenOfListForOxygenList/2):
        mostCommonBit = '1'
    else:
        mostCommonBit = '0'
    l = [x for x in listForOxygen if x[currentBitIndex] == mostCommonBit]
    listForOxygen = l
    currentBitIndex += 1
    positiveBitCounter = 0
    currentLenOfListForOxygenList = len(listForOxygen)

#co2
lessCommonBit = ''
currentLenOfListForCo2List = len(listForCo2)
currentBitIndex = 1
positiveBitCounter = 0

print(currentLenOfListForCo2List)
while(currentLenOfListForCo2List > 1):
    for number in listForCo2:
        if(number[currentBitIndex] == '1'):
            positiveBitCounter += 1

    if(positiveBitCounter < currentLenOfListForCo2List/2):
        lessCommonBit = '1'
    else:
        lessCommonBit = '0'

    print(f'cnt={positiveBitCounter}, len={currentLenOfListForCo2List}, less={lessCommonBit}, index={currentBitIndex}')
    l = [x for x in listForCo2 if x[currentBitIndex] == lessCommonBit]
    listForCo2 = l
    currentBitIndex += 1
    positiveBitCounter = 0
    currentLenOfListForCo2List = len(listForCo2)

print(f'Support rating of submarine is {int(listForCo2[0], 2)*int(listForOxygen[0], 2)}')