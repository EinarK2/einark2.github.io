rows, columns, numBombs = [int(i) for i in input().split()]
bombs = []
for i in range(numBombs):
    bombs.append(tuple([int(i) for i in input().split()]))
for x in range(rows):
    row = ''
    for y in range(columns):
        row += '*' if (x + 1, y + 1) in bombs else '.'
    print(row)