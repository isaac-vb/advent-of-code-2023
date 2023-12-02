import re

puzzle_input = open('day2input.txt', 'r').read().split('\n')

# Part 1


def check_possible_game(line: str):
    NUM_OF_RED_CUBES = 12
    NUM_OF_GREEN_CUBES = 13
    NUM_OF_BLUE_CUBES = 14

    line = line.split(':')

    game_id = int(re.findall(r'\d+', line.pop(0))[0])
    sets = [s.split(",") for s in line[0].replace(" ", "").split(';')]

    for s in sets:
        red_counter = 0
        green_counter = 0
        blue_counter = 0
        for c in s:

            if 'red' in c:
                red_counter += int(re.findall(r'\d+', c)[0])

            elif 'green' in c:
                green_counter += int(re.findall(r'\d+', c)[0])

            elif 'blue' in c:
                blue_counter += int(re.findall(r'\d+', c)[0])

            if (red_counter > NUM_OF_RED_CUBES) or (green_counter > NUM_OF_GREEN_CUBES) or (blue_counter > NUM_OF_BLUE_CUBES):
                return 0

    return game_id


valid_game_ids_sum = 0
for game in puzzle_input:
    valid_game_ids_sum += check_possible_game(game)

print(f"Part 1 Answer: {valid_game_ids_sum}")


# Part 2

def check_min_number_of_cubes(line: str):
    line = line.split(':')

    game_id = int(re.findall(r'\d+', line.pop(0))[0])
    sets = [s.split(",") for s in line[0].replace(" ", "").split(';')]

    red_counts = []
    green_counts = []
    blue_counts = []

    for s in sets:
        for c in s:

            if 'red' in c:
                red_counts.append(int(re.findall(r'\d+', c)[0]))

            elif 'green' in c:
                green_counts.append(int(re.findall(r'\d+', c)[0]))

            elif 'blue' in c:
                blue_counts.append(int(re.findall(r'\d+', c)[0]))

    return max(red_counts) * max(green_counts) * max(blue_counts)


sum_of_powers = 0
for game in puzzle_input:
    sum_of_powers += check_min_number_of_cubes(game)

print(f"Part 2 Answer: {sum_of_powers}")
