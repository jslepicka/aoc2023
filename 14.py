import os

def draw_sketch(s):
    min_x = min(s, key=lambda x:x[0])[0]
    min_y = min(s, key=lambda x:x[1])[1]
    max_x = max(s, key=lambda x:x[0])[0]
    max_y = max(s, key=lambda x:x[1])[1]
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) not in s:
                print(' ', end='')
            else:
                print(s[(x,y)], end='')
        print()

def tilt_dish(dish, tilt_dir):
    #draw_sketch(dish)
    #print()
    max_x = max(dish, key=lambda x:x[0])[0]
    max_y = max(dish, key=lambda x:x[1])[1]

    tilt_dirs = {
        'n': (0, -1),
        'w': (-1, 0),
        's': (0, 1),
        'e': (1, 0)
    }

    maxs = (max_x, max_y)
    xor = 0
    reverse = 0

    if tilt_dir == 'w' or tilt_dir == 'e':
        xor = 1
    if tilt_dir == 's' or tilt_dir == 'e':
        reverse = 1

    zero_xor = 0 ^ xor
    one_xor = 1 ^ xor

    for d1 in range(maxs[zero_xor] + 1):
        for d2 in range(maxs[one_xor] + 1):
            coord = [d1, d2]
            coord = [coord[zero_xor], coord[one_xor]]
            if reverse:
                coord[one_xor] = maxs[one_xor] - coord[one_xor]
            coord = tuple(coord)
            if dish[coord] == 'O':
                orig_coord = coord
                new_coord = coord
                while True:
                    next_coord = (new_coord[0] + tilt_dirs[tilt_dir][0], new_coord[1] + tilt_dirs[tilt_dir][1])
                    if next_coord not in dish or dish[next_coord] != '.':
                        break
                    new_coord = next_coord
                if orig_coord != new_coord:
                    dish[new_coord] = 'O'
                    dish[orig_coord] = '.'
    return dish

def calc_load(dish):
    load = 0
    max_x = max(dish, key=lambda x:x[0])[0]
    max_y = max(dish, key=lambda x:x[1])[1]
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if dish[(x, y)] == 'O':
                load += max_y + 1 - y
    return load

def part1(dish):
    dish = tilt_dish(dish, 'n')
    return calc_load(dish)

def part2(dish):
    i = 0
    d = dish

    seen = {}
    answer_loc = -1
    while True:
        d = tilt_dish(d, 'n')
        d = tilt_dish(d, 'w')
        d = tilt_dish(d, 's')
        d = tilt_dish(d, 'e')
        if i == answer_loc:
            return calc_load(d)
        dval = ''.join(d.values())
        if answer_loc == -1 and dval in seen:
            #print(f'iteration {i} repeats dval from iteration {seen[dval]}')
            cycle_len = i - seen[dval]
            #print(f'cycle length: {cycle_len}')
            answer_loc = ((1_000_000_000 - i) % cycle_len) + i - 1
        seen[dval] = i
        i += 1

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]

    dish = {}
    for y, line in enumerate(input):
        for x, v in enumerate(line):
            dish[(x, y)] = v

    #draw_sketch(dish)
    print("Part 1: " + str(part1(dish)))
    print("Part 2: " + str(part2(dish)))

if __name__ == "__main__":
    main()