filePath = 'data/input.txt'
file = open(filePath, 'r')
lines = file.readlines()
counter = 0
prev = 0

for line in lines:
    if(prev != 0 and int(line) > prev):
        counter += 1
    prev = int(line)

print(f'Increased {counter} times!')
