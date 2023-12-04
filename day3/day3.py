

with open('day3input.txt', 'r') as file:
    puzzle_input = file.read().split('\n')


symbols = set("!#$%&()*+,-/:;<=>?@[\]^_{|}~")

line_number = 1
my_list = []
current_group = ""
current_positions = []
for line in puzzle_input:
    for char_position, char in enumerate(line):
        if char.isnumeric():
            current_group += char
            current_positions.append(char_position)
        elif current_group:
            my_list.append((current_group, current_positions, line_number))
            current_group = ""
            current_positions = []
        if char in symbols:
            my_list.append((char, [char_position], line_number))
    if current_group:
        my_list.append((current_group, current_positions, line_number))
        current_group = ""
        current_positions = []
    line_number += 1


digits_list = [x for x in my_list if x[0].isdigit()]
symbols_list = [x for x in my_list if x[0] in symbols]


def check_horizontal_adjacency(digits_tuple, symbols_tuple):

    if digits_tuple[2] == symbols_tuple[2] and any(abs(x - y) <= 1 for x in digits_tuple[1] for y in symbols_tuple[1]):
        return int(digits_tuple[0])

    else:
        return 0


def check_vertical_adjacency(digits_tuple, symbols_tuple):

    if abs(digits_tuple[2] - symbols_tuple[2]) <= 1 and any(x == symbols_tuple[1][0] for x in digits_tuple[1]):
        return int(digits_tuple[0])

    else:
        return 0


def check_diagonal_adjacency(digits_tuple, symbols_tuple):

    if abs(digits_tuple[2] - symbols_tuple[2]) <= 1 and any(abs(x - y) <= 1 for x in digits_tuple[1] for y in symbols_tuple[1]):
        return int(digits_tuple[0])

    else:
        return 0


total = []
for d in digits_list:
    for s in symbols_list:
        if check_diagonal_adjacency(d, s) != 0:
            total.append(check_diagonal_adjacency(d, s))
        elif check_horizontal_adjacency(d, s) != 0:
            total.append(check_horizontal_adjacency(d, s))
        elif check_vertical_adjacency(d, s) != 0:
            total.append(check_vertical_adjacency(d, s))

print(sum(total))
