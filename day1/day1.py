# Part 1
puzzle_input = open('day1input.txt', 'r').read().split('\n')

total = 0
for line in puzzle_input:
    digits = [l for l in line if l.isdigit()]
    total += int(digits[0]+digits[-1])

print(f"Part 1 Answer: {total}")

# Part 2
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
           'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

total = 0

for line in puzzle_input:

    first_vals = []
    for n in list(numbers.keys())+list(numbers.values()):
        if line.find(str(n)) != -1:
            first_vals.append((n, line.find(str(n))))

    last_vals = []
    for n in list(numbers.keys())+list(numbers.values()):
        if line.rfind(str(n)) != -1:
            last_vals.append((n, line.rfind(str(n))))

    first_value = min(first_vals, key=lambda v: v[1])[0]
    last_value = max(last_vals, key=lambda v: v[1])[0]

    first_value = numbers.get(first_value) if isinstance(
        first_value, str) else first_value
    last_value = numbers.get(last_value) if isinstance(
        last_value, str) else last_value

    total += int(str(first_value)+str(last_value))


print(f"Part 2 Answer: {total}")
