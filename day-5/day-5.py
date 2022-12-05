# Meal prep
input = open("./input", "r")
lines = input.readlines()

# Parse Stacks
column_count = int(len(lines[0])) // 4

crate_input: list[str] = []
for line in lines:
    if "1" in line:
        break
    crate_input.append(line)


def parse_layers(column: int, lines: list[str]) -> list[str]:
    stack: list[str] = []
    for line in lines:
        if line[column * 4] == " ":
            continue
        stack += line[column * 4 + 1]

    return stack


stacks: list[list[str]] = []
for column in range(0, column_count):
    stacks.append(parse_layers(column, crate_input))

# Parse instructions
import re

moves: list[list[int]] = []
for line in lines:
    if "move" in line:
        # Yeah try understanding this line after a few beers
        m = [int(x.group(0)) for x in re.finditer(r"\d+", line)]

        moves.append(m)

# Part 1

part_one_stacks = [x.copy() for x in stacks]
for [quantity, source, destination] in moves:
    for _ in range(0, quantity):
        crate = part_one_stacks[source - 1].pop(0)
        part_one_stacks[destination - 1].insert(0, crate)

print(f' Part 1: {"".join([x[0] for x in part_one_stacks])}')

# Part 2

part_two_stacks = [x.copy() for x in stacks]
for [quantity, source, destination] in moves:

    crates = part_two_stacks[source - 1][:quantity]

    part_two_stacks[source - 1] = part_two_stacks[source - 1][quantity:]

    part_two_stacks[destination - 1] = crates + part_two_stacks[destination - 1]

print(f' Part 2: {"".join([x[0] for x in part_two_stacks])}')
