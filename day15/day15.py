import re


def load_puzzle_input():
    with open('day15input.txt', 'r') as file:
        puzzle_input = file.read().split(',')

    return puzzle_input


def hash_algorithm(string):
    hash_algorithm_value = 0
    for c in string:
        hash_algorithm_value += ord(c)
        hash_algorithm_value = hash_algorithm_value*17
        hash_algorithm_value = hash_algorithm_value % 256
    return hash_algorithm_value


puzzle = load_puzzle_input()

# Part 1
total = 0
for p in puzzle:
    total += hash_algorithm(p)

print(f"Part 1 Answer: {total}")

# Part 2
box_dict = {}
for x in range(0, 256):
    box_dict[x] = []


def dash(box_dict, operation):
    lens = "".join(re.findall("[a-zA-Z]+", operation))

    for box, elements in box_dict.items():
        if any(lens == e[0] for e in elements):
            elements[:] = [t for t in elements if t[0] != lens]


def equals(box_dict, operation):
    lens = "".join(re.findall("[a-zA-Z]+", operation))
    focal_length = "".join(re.findall(r'\d+', operation))
    destination_box = hash_algorithm(lens)

    if lens in [l[0] for l in box_dict[destination_box]]:
        for i, x in enumerate(box_dict[destination_box]):
            if x[0] == lens:
                box_dict[destination_box][i] = (lens, focal_length)

    else:
        box_dict[destination_box].append((lens, focal_length))


for p in load_puzzle_input():
    if "=" in p:
        equals(box_dict, p)
    else:
        dash(box_dict, p)


total = 0

for b in box_dict.items():
    if b[1] != []:
        box_num = b[0]+1
        positions_and_lens = [(pos+1, int(lenses[1]))
                              for pos, lenses in enumerate(b[1])]
        for info in positions_and_lens:
            total += (box_num * info[0] * info[1])

print(f"Part 2 Answer {total}")
