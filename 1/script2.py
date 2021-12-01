# read all lines, save three consecutive values to list, while next value is fourth,
# compare if the sum of elements 0, 1 and 2 are lower than sum of elements 1,2 and currently read value as integer

filePath = 'data/input.txt'
file = open(filePath, 'r')
lines = file.readlines()
counter = 0
tab = [0,0,0]

for line in lines:
    if(tab[0] != 0 and tab[1] != 0 and tab[2] != 0 and tab[0] + tab[1] + tab[2] < tab[1] + tab[2] + int(line)):
        counter += 1

    tab[0] = tab[1]
    tab[1] = tab[2]
    tab[2] = int(line)

print(f'Three measurements increased {counter} times!')
