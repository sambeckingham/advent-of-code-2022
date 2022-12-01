input = open('./input', 'r')
lines = input.readlines()

# Part 1
elves = []
current_elf_total = 0
for line in lines:
  if len(line.strip()) > 0:
    current_elf_total += int(line)
  else:
    elves.append(current_elf_total)
    current_elf_total = 0

print(max(elves))

# Part 2
fattest_elves = sorted(elves, reverse=True)[:3]
print(sum(fattest_elves))