import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, help="For cycle range int value")
args = parser.parse_args()
for _ in range(args.n):
    line = sys.stdin.readline().rstrip()
    if len(line) == 32:
        if line[0:5] == "00000" and line[5] != '0':
            print(line)
