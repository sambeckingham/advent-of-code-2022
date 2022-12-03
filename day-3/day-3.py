input = open("./input", "r")
lines = input.readlines()


def get_letter_priority(letter: str) -> int:
    if ord(letter) <= 90:
        return ord(letter) - 38
    else:
        return ord(letter) - 96


# Part 1
total: int = 0
for line in lines:
    line = list(line.strip())

    firstHalf = set(line[: len(line) // 2])
    secondHalf = set(line[len(line) // 2 :])

    priorityItem = firstHalf.intersection(secondHalf).pop()

    total += get_letter_priority(priorityItem)

print("Part 1: %d" % total)

# Part 2

total: int = 0
groupSize: int = 3
groupList: list[set[str]] = []
for line in lines:
    groupList.append(set(line.strip()))

    if len(groupList) == groupSize:
        badgeLetter = set.intersection(*groupList).pop()
        total += get_letter_priority(badgeLetter)
        groupList = []


print("Part 2: %d" % total)
