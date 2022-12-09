
FILE_PATH = "z:/home/alangley/Sandbox/Advent/day2/input.txt"
f = open(FILE_PATH, 'r')

lines = f.readlines()

# A Rock
# B Paper
# C Scissors
# X Rock     - 1
# Y Paper    - 2
# Z Scissors - 3
# Lose  - 0
# Draw  - 3 
# Win   - 6

score = 0
LOSE = 0
DRAW = 3
WIN = 6
ROCK = 1
PAPER = 2
SCISSORS = 3

for line in lines:
    abc = line[0]
    xyz = line[2]
    if (abc == 'A'):
        if (xyz == 'X'):
            score = score + LOSE
            score = score + SCISSORS
        if (xyz == 'Y'):
            score = score + DRAW
            score = score + ROCK
        if (xyz == 'Z'):
            score = score + WIN
            score = score + PAPER
    if (abc == 'B'):
        if (xyz == 'X'):
            score = score + LOSE
            score = score + ROCK
        if (xyz == 'Y'):
            score = score + DRAW
            score = score + PAPER
        if (xyz == 'Z'):
            score = score + WIN
            score = score + SCISSORS
    if (abc == 'C'):
        if (xyz == 'X'):
            score = score + LOSE
            score = score + PAPER
        if (xyz == 'Y'):
            score = score + DRAW
            score = score + SCISSORS
        if (xyz == 'Z'):
            score = score + WIN
            score = score + ROCK

print(score)









