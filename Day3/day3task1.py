filePath = 'input.txt'
file = open(filePath, 'r')
lines = file.readlines()
gammaRate = ''
epsilonRate = ''
positiveBitCounterList = []
isInitialized = False
lengthOfLine = 0
linesCounter = 0

for line in lines:
    if(isInitialized == False):
        lengthOfLine = len(line.strip())
        positiveBitCounterList = [0]*lengthOfLine
        isInitialized = True

    for i in range(0, lengthOfLine):
        if(line[i] == '1'):
            positiveBitCounterList[i] += 1
    linesCounter += 1

for bit in positiveBitCounterList:
    if(bit >= linesCounter/2):
        gammaRate += '1'
        epsilonRate += '0'
        continue
    gammaRate += '0'
    epsilonRate += '1'

print(f'The power consuption of the submarine is {int(gammaRate, 2) * int(epsilonRate, 2)}')