filePath = 'input.txt'
fishesRaw = []

# Read file and set init state
with open(filePath, 'r') as file:
    line = file.readline()
    temp = line.strip().split(',')
    for i in range(0, len(temp)):
        fishesRaw.append(int(temp[i]))

# Create new list which represents amount of fishes that have given timer
fishes = [0 for i in range(0, 9)]
maxValueInInput = 5
minValueInInpiut = 1
for x in range(1, len(fishes)):
    fishes[x] = len(list(filter(lambda numb: numb == x, fishesRaw)))

# Simulate lanternfish
days = 256
for i in range(0, days):
    toAdd = 0
    for j in range(0, len(fishes)):
        amountOfFishes = fishes[j]
        if(j == 0):
            toAdd = amountOfFishes
            fishes[j] = 0
            continue

        fishes[j-1] = amountOfFishes
        fishes[j] = 0
    fishes[6] += toAdd
    fishes[8] += toAdd
sum = 0
for f in fishes:
    sum += f
print(sum)