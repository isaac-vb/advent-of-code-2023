from collections import Counter

with open('day7input.txt', 'r') as file:
    puzzle_input = file.read().split('\n')
    puzzle_input = [p.split(" ") for p in puzzle_input]
    puzzle_input = [[p[0], int(p[1])] for p in puzzle_input]


camel_cards_game = []
for p in puzzle_input:
    camel_cards_dict = {}
    camel_cards_dict['hand'] = p[0]
    camel_cards_dict['bid'] = p[1]
    camel_cards_game.append(camel_cards_dict)

CARD_TYPES = ["A", "K", "Q", "J", "T",
              "9", "8", "7", "6", "5", "4", "3", "2"]
CARD_TYPES.reverse()


def calculate_hand_type(hand: str, part: int):
    """Calculates the hand type of a given hand, also based on the part of the question"""
    card_counts = dict(sorted(dict(Counter(hand)).items(),
                       key=lambda x: x[1], reverse=True))

    if part == 2:
        if "J" in card_counts:
            if len(card_counts) == 1:
                return 7
            else:
                card_counts = joker_sorting(card_counts)

    # Five of a kind
    if len(card_counts) == 1:
        return 7

    # Four of a kind
    elif list(card_counts.values()) == [4, 1]:
        return 6

    # Full house
    elif list(card_counts.values()) == [3, 2]:
        return 5

    # Three of a kind
    elif list(card_counts.values()) == [3, 1, 1]:
        return 4

    # Two pair
    elif list(card_counts.values()) == [2, 2, 1]:
        return 3

    # One pair
    elif list(card_counts.values()) == [2, 1, 1, 1]:
        return 2

    # High card
    elif len(card_counts) == 5:
        return 1


def sort_by_score(item):
    """Sorts the hands by their score followed by the individual card ranks"""
    hand_score = item['hand_score']
    card_values = [CARD_TYPES.index(card) for card in item['hand']]

    return (hand_score, *card_values)


def joker_sorting(card_counts: dict):
    """Converts the joker cards in a hand accordingly"""
    joker_card_count = card_counts.get("J")
    del card_counts["J"]

    max_occurences = {card: count for card, count in card_counts.items(
    ) if count >= max(card_counts.values())}

    most_common_card = list(max_occurences.keys())[0]

    card_counts[most_common_card] += joker_card_count

    return card_counts


# Part 1
for c in camel_cards_game:
    c['hand_score'] = calculate_hand_type(c.get('hand'), part=1)

camel_cards_game = sorted(camel_cards_game, key=sort_by_score)

total_winnings = 0
for rank, c in enumerate(camel_cards_game):
    c['rank'] = rank+1
    total_winnings += c.get('bid') * c.get('rank')

print(f"Part 1 Answer: {total_winnings}")

# Part 2

# Adjust the card type rankings (for the joker card)
CARD_TYPES = ["A", "K", "Q", "T",
              "9", "8", "7", "6", "5", "4", "3", "2", "J"]
CARD_TYPES.reverse()

for c in camel_cards_game:
    c['hand_score'] = calculate_hand_type(c.get('hand'), part=2)

camel_cards_game = sorted(camel_cards_game, key=sort_by_score)

total_winnings = 0
for rank, c in enumerate(camel_cards_game):
    c['rank'] = rank+1
    total_winnings += c.get('bid') * c.get('rank')

print(f"Part 2 Answer: {total_winnings}")
