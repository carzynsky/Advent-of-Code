# read all lines, cast to integer check if current value is higher than previous
# if yes then increment counter

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
