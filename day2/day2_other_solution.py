"""Alternative solution for day 2"""
import re

with open('day2input.txt', 'r') as file:
    puzzle_input = file.read().split('\n')


NUM_OF_RED_CUBES = 12
NUM_OF_GREEN_CUBES = 13
NUM_OF_BLUE_CUBES = 14


def get_game_info(line: str):
    line = line.split(':')

    digits = re.compile(r'\d+')

    game_id = int(digits.findall(line.pop(0))[0])
    sets = [s.split(",") for s in line[0].replace(" ", "").split(';')]

    max_red_count = 0
    max_green_count = 0
    max_blue_count = 0

    for s in sets:
        for c in s:

            if 'red' in c:
                red_count = int(digits.findall(c)[0])
                if red_count > max_red_count:
                    max_red_count = red_count

            if 'green' in c:
                green_count = int(digits.findall(c)[0])
                if green_count > max_green_count:
                    max_green_count = green_count

            elif 'blue' in c:
                blue_count = int(digits.findall(c)[0])
                if blue_count > max_blue_count:
                    max_blue_count = blue_count

    return {"game_id": game_id, "max_red_cubes": max_red_count, "max_green_cubes": max_green_count, "max_blue_cubes": max_blue_count}


# Part 1:

valid_game_ids_sum = 0
for game in puzzle_input:
    game_info = get_game_info(game)

    if all(x <= y for x, y in zip((game_info['max_red_cubes'], game_info['max_green_cubes'], game_info['max_blue_cubes']), (NUM_OF_RED_CUBES, NUM_OF_GREEN_CUBES, NUM_OF_BLUE_CUBES))):
        valid_game_ids_sum += game_info['game_id']

print(f"Part 1 Answer: {valid_game_ids_sum}")

# Part 2:
sum_of_power_sets = sum(
    game_info['max_red_cubes'] * game_info['max_green_cubes'] *
    game_info['max_blue_cubes']
    for game_info in (get_game_info(game) for game in puzzle_input)
)

print(f"Part 2 Answer: {sum_of_power_sets}")
