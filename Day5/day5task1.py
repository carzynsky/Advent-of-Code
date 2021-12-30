filePath = 'input.txt'
dim = 1000
diagramMatrix = []

# prepare diagram Matrix
for i in range(0,dim):
    diagramMatrix.append([0]*dim)

with open(filePath, 'r') as file:
    lines = file.readlines()
    for line in lines:
        tab = line.strip().replace(' -> ', ',').split(',')
        # x1, x2
        if(tab[0] == tab[2]):
            diff = int(tab[1]) - int(tab[3])
            sign = -1
            if(diff < 0 ):
                sign = sign*(-1)
            for i in range(0,abs(diff)+1):
                diagramMatrix[int(tab[0])][int(tab[1]) + sign*i] += 1
        # y1, y2    
        elif(tab[1] == tab[3]):
            diff = int(tab[0]) - int(tab[2])
            sign = -1
            if(diff < 0 ):
                sign = sign*(-1)
            for i in range(0,abs(diff)+1):
                diagramMatrix[int(tab[0])+sign*i][int(tab[1])] += 1

overlapCounter = 0
for row in diagramMatrix:
    for col in row:
        if(col > 1):
            overlapCounter += 1

print(f'The number of points where at least two lines overlap = {overlapCounter}')



