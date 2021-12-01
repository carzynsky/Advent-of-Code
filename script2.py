filePath = 'data/input.txt'
file = open(filePath, 'r')
lines = file.readlines()
counter = 0
x = 0
y = 0
z = 0

for line in lines:
    if(x != 0 and y != 0 and z != 0 and x + y + z < y + z + int(line)):
        counter += 1

    x = y
    y = z
    z = int(line)

print(f'Three measurements increased {counter} times!')
