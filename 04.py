import os

def part1(input):
    total_points = 0
    for i in input:
        card, numbers = i.split(':')
        winning_numbers, my_numbers = numbers.split('|')
        winning_numbers = set([int(x) for x in winning_numbers.strip().split()])
        my_numbers = set([int(x) for x in my_numbers.strip().split()])
        #print(f'{card} {winning_numbers} {my_numbers}')
        winners = my_numbers & winning_numbers
        #print(winners)
        if num_winners := len(winners):
            points = 2**(num_winners-1)
            total_points += points
        #print(points)
    return total_points

def part2(input):
    card_set = {}
    for i, c in enumerate(input):
        card_set[i+1] = {
            "copies": 1,
            "card": c
        }
    for i in sorted(card_set.keys()):
        copies = card_set[i]["copies"]
        #print(f'{i} {copies}')
        c = card_set[i]['card']
        card, numbers = c.split(':')
        winning_numbers, my_numbers = numbers.split('|')
        winning_numbers = set([int(x) for x in winning_numbers.strip().split()])
        my_numbers = set([int(x) for x in my_numbers.strip().split()])
        #print(f'{card} {winning_numbers} {my_numbers}')
        winners = my_numbers & winning_numbers
        #print(winners)
        for x in range(len(winners)):
            n = x + i + 1
            #print(".")
            if n in card_set:
                card_set[n]['copies'] += copies

    total_cards = sum([v['copies'] for k, v in card_set.items()])
    return total_cards

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()