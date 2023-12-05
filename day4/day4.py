# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1

import re
# Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
# Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
# Card 4 has one winning number (84), so it is worth 1 point.
# Card 5 has no winning numbers, so it is worth no points.
# Card 6 has no winning numbers, so it is worth no points.
# So, in this example, the Elf's pile of scratchcards is worth 13 points.

input = "Card 14: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
input = "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"

with open('day4input.txt', 'r') as file:
    puzzle_input = file.read().split('\n')

input = puzzle_input


def get_info_from_card(card):
    card = card.split(":")

    card_number = int(re.findall(r'\d+', card.pop(0))[0])

    numbers = "".join(card).split("|")
    winning_numbers = [int(n) for n in re.findall(r'\d+', numbers[0])]
    played_numbers = [int(n) for n in re.findall(r'\d+', numbers[1])]

    return {"card_number": card_number, "winning_numbers": winning_numbers, "played_numbers": played_numbers}


def calculate_points_for_card(winning_numbers, played_numbers):

    matched_numbers = [n for n in played_numbers if n in winning_numbers]

    if len(matched_numbers) == 1:
        return 1
    elif len(matched_numbers) > 1:
        return pow(2, len(matched_numbers)-1)
    return 0


# Part 1
total_points = 0
for card in puzzle_input:
    card_info = get_info_from_card(card)
    winning_numbers = card_info.get("winning_numbers")
    played_numbers = card_info.get("played_numbers")

    total_points += calculate_points_for_card(winning_numbers, played_numbers)


print(f"Part 1 Answer: {total_points}")
