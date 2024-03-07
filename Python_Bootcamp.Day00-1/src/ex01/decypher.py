import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        line = sys.argv[1]
        for i in line.split():
            print(i[0], end='')
