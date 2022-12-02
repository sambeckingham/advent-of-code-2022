input = open('./input', 'r')
lines = input.readlines()

# Part 1

outcomes: dict[str, int] = { 
      'A X': 4, 'A Y': 8, 'A Z': 3,
      'B X': 1, 'B Y': 5, 'B Z': 9,
      'C X': 7, 'C Y': 2, 'C Z': 6,
}

total: int = 0

for line in lines:
    total += outcomes[line.strip()]

print(total)


# Part 2

actualOutcomes: dict[str, int] = { 
      'A X': 3, 'A Y': 4, 'A Z': 8,
      'B X': 1, 'B Y': 5, 'B Z': 9,
      'C X': 2, 'C Y': 6, 'C Z': 7,
}

actualTotal: int = 0

for line in lines:
    actualTotal += actualOutcomes[line.strip()]

print(actualTotal)
