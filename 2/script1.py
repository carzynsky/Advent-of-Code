filePath = '2/data/input.txt'
file = open(filePath, 'r')
lines = file.readlines()
horizontalPosition = 0
depth = 0

# read all lines, check instruction after split of data and add/substract depth, add horizontalPosition
for line in lines:
    data = line.split()
    if(data[0] == 'forward'):
        horizontalPosition += int(data[1])
    elif(data[0] == 'up'):
        depth -= int(data[1])
    else:
        depth += int(data[1])

print(f'Horizontal position={horizontalPosition} * depth={depth} = {horizontalPosition*depth}')

