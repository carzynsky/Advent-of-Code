filePath = '2/data/input.txt'
file = open(filePath, 'r')
lines = file.readlines()
horizontalPosition = 0
depth = 0
aim = 0

for line in lines:
    data = line.split()
    if(data[0] == 'forward'):
        horizontalPosition += int(data[1])
        depth += int(data[1])*aim
    elif(data[0] == 'up'):
        aim -= int(data[1])
    else:
        aim += int(data[1])

print(f'Horizontal position={horizontalPosition} * depth={depth} = {horizontalPosition*depth}')

