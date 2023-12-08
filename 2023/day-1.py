# Advent of code Day 1 | 2023
# https://adventofcode.com/2023/day/1
print("Advent of code Day 1 | 2023\n")
with open("input/day-1.txt", "r") as file:
    lines = file.readlines()

correct = []
for line in lines:
    numbers = [int(char) for char in line if char.isdigit()]

    if len(numbers) >= 1:
        first_number = numbers[0]
        if len(numbers) > 1:
            last_number = numbers[-1]
            result = first_number * 10 + last_number
        else:
            result = first_number * 11  
        correct.append(result)

print(sum(correct))




