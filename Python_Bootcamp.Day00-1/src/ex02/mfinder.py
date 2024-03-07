import sys

lines = [i.strip() for i in sys.stdin.readlines()]
snow_flake = {0: [0, 4], 1: [0, 1, 3, 4], 2: [0, 2, 4]}
if len(lines) == 3 and all([i == 5 for i in list(map(len, lines))]):
    print(all([all([lines[i][j] == '*' if j in snow_flake[i] else lines[i][j] != '*'
                    for j in range(5)]) for i in range(3)]))
else:
    print("Ошибка")
