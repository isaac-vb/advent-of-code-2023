import re
import math


def process_puzzle_input():
    with open('day6input.txt', 'r') as file:
        puzzle_input = file.read().split('\n')

    return puzzle_input


def get_total_distance_possibilities(race_info: tuple):
    race_time = race_info[0]
    race_record_distance = race_info[1]

    distances = []

    # Ignore zero and race_time values as they lead to zero distance
    for x in range(1, race_time):
        distances.append((race_time - x) * x)

    return len([d for d in distances if d > race_record_distance])


def part_1(puzzle_input):
    times = [int(t) for t in re.findall(r'\d+', puzzle_input[0])]
    record_distances = [int(d) for d in re.findall(r'\d+', puzzle_input[1])]
    races_info = list(zip(times, record_distances))

    possibilities_to_beat_race = []
    for race in races_info:
        possibilities_to_beat_race.append(
            get_total_distance_possibilities(race))

    return math.prod(possibilities_to_beat_race)


def part_2(puzzle_input):
    time = int("".join([t for t in re.findall(r'\d+', puzzle_input[0])]))
    distance = int(
        "".join([t for t in re.findall(r'\d+', puzzle_input[1])]))

    total_possibilities_to_beat_record = get_total_distance_possibilities(
        (time, distance))

    return total_possibilities_to_beat_record


puzzle_input = process_puzzle_input()


print("Part 1 Answer: ", part_1(puzzle_input))
print("Part 2 Answer: ", part_2(puzzle_input))
