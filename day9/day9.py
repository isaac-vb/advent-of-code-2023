import re


def load_puzzle_input():

    with open('day9input.txt', 'r') as file:
        puzzle_input = file.read().split('\n')

    puzzle_input = [[int(num) for num in re.findall("-?\d+", line)]
                    for line in puzzle_input]
    return puzzle_input


def get_differences_sequence(history_list: list):

    all_lists = [history_list]
    while set(history_list) != set([0]):
        history_list = [history_list[index+1] - history_list[index]
                        for index in range(len(history_list[:-1]))]
        all_lists.append(history_list)

    all_lists.reverse()
    return all_lists


def get_next_history_value(differences_sequence: list):

    for x in range(0, len(differences_sequence)-1):
        differences_sequence[x+1].append(
            (differences_sequence[x][-1] + differences_sequence[x+1][-1]))
    return differences_sequence[-1][-1]


def get_previous_history_value(differences_sequence: list):

    for x in range(0, len(differences_sequence)-1):
        differences_sequence[x+1].insert(0, differences_sequence[x+1]
                                         [0] - differences_sequence[x][0])
    return differences_sequence[-1][0]


puzzle_input = load_puzzle_input()


# Part 1
total = 0
for p in puzzle_input:
    total += get_next_history_value(get_differences_sequence(p))

print(f"Part 1 Answer: {total}")

# Part 2
total = 0
for p in puzzle_input:
    total += get_previous_history_value(get_differences_sequence(p))

print(f"Part 2 Answer: {total}")
