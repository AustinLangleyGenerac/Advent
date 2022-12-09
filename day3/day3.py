
FILE_PATH = "z:/home/alangley/Sandbox/Advent/day3/input.txt"
f = open(FILE_PATH, 'r')

lines = f.readlines()

# a = 97
# A - 65

sum = 0
count = 1
string1 = ""
string2 = ""
string3 = ""

for line in lines:
    if (count == 1):
        string1 = line
        count = count + 1
    elif (count == 2):
        string2 = line
        count = count + 1
    elif (count == 3):
        string3 = line
        count = 1
        for x in string1:
            if x in string2:
                if x in string3:
                    # print("Found " + x + " " + str(ord(x)))
                    val = ord(x)
                    if (val > 95):
                        val = val - 96
                    else:
                        val = val - 38
                    sum = sum + val
                    break
                    
print(sum)