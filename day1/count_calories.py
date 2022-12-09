

ELVES_FILE_PATH = "z:/home/alangley/Sandbox/Advent/day1/input.txt"
elves = open(ELVES_FILE_PATH, 'r')

lines = elves.readlines()

current_elf_cals = 0
third_highest_elf_cals = 0
second_highest_elf_cals = 0
first_highest_elf_cals = 0
new_elf = False

for line in lines:
    number = line.strip()
    if (number == ""):
        new_elf = True
    else:
        current_elf_cals = current_elf_cals + int(number)
    
    if (new_elf):
        new_elf = False
        if current_elf_cals > first_highest_elf_cals:
            third_highest_elf_cals = second_highest_elf_cals
            second_highest_elf_cals = first_highest_elf_cals
            first_highest_elf_cals = current_elf_cals
        elif current_elf_cals > second_highest_elf_cals:
            third_highest_elf_cals = second_highest_elf_cals
            second_highest_elf_cals = current_elf_cals
        elif current_elf_cals > third_highest_elf_cals:
            third_highest_elf_cals = current_elf_cals

        current_elf_cals = 0

if current_elf_cals > first_highest_elf_cals:
    third_highest_elf_cals = second_highest_elf_cals
    second_highest_elf_cals = first_highest_elf_cals
    first_highest_elf_cals = current_elf_cals
elif current_elf_cals > second_highest_elf_cals:
    third_highest_elf_cals = second_highest_elf_cals
    second_highest_elf_cals = current_elf_cals
elif current_elf_cals > third_highest_elf_cals:
    third_highest_elf_cals = current_elf_cals

print(third_highest_elf_cals)
print(second_highest_elf_cals)
print(first_highest_elf_cals)

print(third_highest_elf_cals + second_highest_elf_cals + first_highest_elf_cals)
