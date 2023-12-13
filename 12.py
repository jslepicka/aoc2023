import os
from functools import cache

@cache
def get_arrangements(field, counts, prev_match = 0):
    #print(f'{field} {counts}')
    if len(field) < (sum(counts) + len(counts) - 1):
        return 0
    if field[0] == '?':
        a = get_arrangements(field[1:], counts)
        b = 0 if prev_match else get_arrangements('#' + field[1:], counts)
        return a + b
    elif field[0] == '#':
        if '.' in field[0:counts[0]]:
            return 0
        if len(field) == counts[0] or field[counts[0]] != '#':
            new_counts = tuple(counts[1:])
            new_field = field[counts[0]:]
            if len(new_counts) == 0:
                if '#' not in new_field:
                    return 1
                return 0
            return get_arrangements(new_field, new_counts, 1)
        else:
            return 0
    else:
        return get_arrangements(field[1:], counts)

def part1(input):
    s = 0
    for i in input:
        field = i['field']
        counts = i['counts']
        s += get_arrangements(field, counts)
    return s

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    input2 = []
    with open(day + ".txt") as file:
        for line in [x.strip() for x in file.readlines()]:
            field, counts = line.split()
            x = {}
            x['field'] = field
            counts = [int(c) for c in counts.split(',')]
            x['counts'] = tuple(counts)
            input.append(x)
            part2_field = ""
            part2_counts = []
            for i in range(5):
                if i != 0:
                    part2_field += "?"
                part2_field += field
                part2_counts.extend(counts)
            y = {}
            y['field'] = part2_field
            y['counts'] = tuple(part2_counts)
            input2.append(y)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part1(input2)))
    print(get_arrangements.cache_info())

if __name__ == "__main__":
    main()