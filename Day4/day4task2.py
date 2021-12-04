filePath = 'input.txt'
order = []
startedReadingMatrix = False
bingoBoards = []
tempMatrix = []
counter = 0

# load data
with open(filePath, 'r') as file:
    order = file.readline().strip().split(',')
    lines = file.readlines()
    for line in lines:
        if(line == '\n'):
            continue
        tempLine = line.strip().split()
        tempMatrix.append(tempLine)
        counter += 1
        if(counter == 5):
            if(len(tempMatrix) > 0):
                bingoBoards.append(tempMatrix)
            tempMatrix = []
            counter = 0
            continue

isWinnerFound = False
winningOrderNumber = 0
winnerMatrix = []
orderCnt = 0
indexesOfWinners = []
for number in order:
    orderCnt += 1
    i = 0
    j = 0
    k = 0
    for board in bingoBoards:
        j = 0
        if(not indexesOfWinners.__contains__(i)):
            for row in board:
                k = 0
                for col in row:
                    if(number == col):
                        bingoBoards[i][j][k] = 'X'
                    k += 1
                j += 1
        i += 1
    if(orderCnt >= 5):
        i = 0
        j = 0
        k = 0
        for board in bingoBoards:
            # row check
            for row in board:
                if(row == ['X']*5 and not indexesOfWinners.__contains__(i)):
                    indexesOfWinners.append(i)
                    winnerMatrix = board
                    winningOrderNumber  = number
                    break
            # column check
            for x in range(0, 5):
                if(board[0][x] == 'X' and board[1][x] == 'X' and board[2][x] == 'X' and board[3][x] == 'X' and board[4][x] == 
                'X' and not indexesOfWinners.__contains__(i)):
                    winnerMatrix = board
                    indexesOfWinners.append(i)
                    winningOrderNumber = number
                    break
            i += 1

lastWinnerIndex = indexesOfWinners[len(indexesOfWinners)-1]
sum = 0
for row in bingoBoards[lastWinnerIndex]:
    for col in row:
        if(col != 'X'):
            sum += int(col)

print(sum, winningOrderNumber)
print(f'Sum({sum}) * winningNumber({winningOrderNumber}) = {sum*int(winningOrderNumber)}')