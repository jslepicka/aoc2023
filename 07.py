import os
from functools import cmp_to_key, cache
from collections import Counter

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0

@cache
def get_hand_value(hand):
    hand = hand.replace('X', '')
    number_of_jokers = 5 - len(hand)
    if number_of_jokers == 5:
        return FIVE_OF_A_KIND
    c = Counter(hand)
    most_frequent_card = max(c, key=c.get)
    c[most_frequent_card] += number_of_jokers

    if 5 in c.values():
        return FIVE_OF_A_KIND
    elif 4 in c.values():
        return FOUR_OF_A_KIND
    elif 3 in c.values() and 2 in c.values():
        return FULL_HOUSE
    elif 3 in c.values():
        return THREE_OF_A_KIND
    elif 2 in Counter([x for x in c.values() if x == 2]).values():
        return TWO_PAIR
    elif 2 in c.values():
        return ONE_PAIR
    else:
        return HIGH_CARD

def cmp_tied_hands(a, b):
    vals = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        'X': 0
    }
    for card_a, card_b in zip(a, b):
        card_a = int(card_a) if card_a.isnumeric() else vals[card_a]
        card_b = int(card_b) if card_b.isnumeric() else vals[card_b]
        if (card_a > card_b):
            return -1
        elif (card_b > card_a):
            return 1
    return 0

def cmp_hands(a, b):
    #print(f'{a} {b}')
    a_val = get_hand_value(a[0])
    b_val = get_hand_value(b[0])

    if (a_val == b_val):
        #print(f'{a} and {b} are equal, run second rule')
        hands_sorted = sorted([a[0], b[0]], key=cmp_to_key(cmp_tied_hands))
        if hands_sorted[0] == a[0]:
            return -1
        elif hands_sorted[0] == b[0]:
            return 1

    return (a_val < b_val) - (a_val > b_val)

def part1(hands):
    hands_sorted = reversed(sorted(hands.items(), key=cmp_to_key(cmp_hands)))
    ret = 0
    for rank, hand in enumerate(hands_sorted, start = 1):
        ret += rank * int(hand[1])

    return ret

def part2(hands):
    hands_sorted = reversed(sorted([(h.replace('J', 'X'), b) for h, b in hands.items()], key=cmp_to_key(cmp_hands)))
    ret = 0
    for rank, hand in enumerate(hands_sorted, start = 1):
        ret += rank * int(hand[1])

    return ret

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]

    hands = {}
    for i in input:
        hand, bid = i.split()
        hands[hand] = bid

    print("Part 1: " + str(part1(hands)))
    print("Part 2: " + str(part2(hands)))

if __name__ == "__main__":
    main()