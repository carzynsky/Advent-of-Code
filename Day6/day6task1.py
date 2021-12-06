filePath = 'input.txt'
fishes = []

# Read file and set init state
with open(filePath, 'r') as file:
    line = file.readline()
    temp = line.strip().split(',')
    for i in range(0, len(temp)):
        fishes.append(int(temp[i]))

# Simulate lanternfish
days = 80
for i in range(0, days):
    currentFishes = len(fishes)
    for j in range(0, currentFishes):
        if(fishes[j] > 0):
            fishes[j] -= 1
            continue
        fishes[j] = 6
        fishes.append(8)
    print(f'Day {i+1}...')

print(len(fishes))