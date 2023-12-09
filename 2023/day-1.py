# Advent of code Day 1 | 2023
# https://adventofcode.com/2023/day/1
print("Advent of code Day 1 | 2023\n")

with open("2023/input/day-1.txt", "r") as file:
    lines = file.readlines()

# Part 1
correct_part1 = 0
for line in lines:
    num = []
    for char in line.strip():
        if not char.isdigit():
            continue
        if len(num) < 2:
            num.append(char)
        else:
            num[-1] = char
    if 0 < len(num) < 2:
        num.append(num[0])
    if num:
        correct_part1 += int("".join(num))

print(f"[PART 1] Result: {correct_part1}")

# Part 2
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total_sum = 0

def verify(line):
    for num, digit in enumerate(digits):
        if line.startswith(digit):
            return str(num + 1)
    return None

for line in lines:
    num = []
    for ind, char in enumerate(line):
        if not char.isdigit():
            if not (char := verify(line[ind:])):
                continue
        if len(num) < 2:
            num.append(char)
        else:
            num[-1] = char
    if 0 < len(num) < 2:
        num.append(num[0])
    total_sum += int("".join(num))

print(f"[PART 2] Result: {total_sum}")

