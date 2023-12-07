import re

with open('day4input.txt', 'r') as file:
    puzzle_input = file.read().split('\n')


def get_info_from_card(card):
    card = card.split(":")

    card_number = int(re.findall(r'\d+', card.pop(0))[0])

    numbers = "".join(card).split("|")
    winning_numbers = [int(n) for n in re.findall(r'\d+', numbers[0])]
    played_numbers = [int(n) for n in re.findall(r'\d+', numbers[1])]
    matched_numbers = [n for n in played_numbers if n in winning_numbers]

    return {"card_number": card_number, "winning_numbers": winning_numbers, "played_numbers": played_numbers, "matched_numbers": matched_numbers}


def calculate_points_for_card(matched_numbers):
    if len(matched_numbers) == 1:
        return 1
    elif len(matched_numbers) > 1:
        return pow(2, len(matched_numbers)-1)
    return 0


# Part 1
total_points = 0
for card in puzzle_input:
    card_info = get_info_from_card(card)
    matched_numbers = card_info.get("matched_numbers")

    total_points += calculate_points_for_card(matched_numbers)


print(f"Part 1 Answer: {total_points}")

# Part 2


def check_copies_won(card_info):
    number_of_matches = len(card_info.get('matched_numbers'))
    card_number = card_info.get('card_number')
    if number_of_matches != 0:
        return list(range(card_number+1, card_number + number_of_matches+1))

    return 0


puzzle_input = [get_info_from_card(c) for c in puzzle_input]


for p in puzzle_input:
    p['copies'] = 1

for card in puzzle_input:
    copies_won = check_copies_won(card)
    if copies_won != 0:
        for c in copies_won:
            for entry in puzzle_input:
                if entry.get('card_number') == c:
                    entry['copies'] += card['copies']


total_scratchcards = sum(entry["copies"] for entry in puzzle_input)
print(f"Part 2 Answer: {total_scratchcards}")
