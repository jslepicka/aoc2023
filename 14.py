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
    new_dish = dish.copy()
    for k, v in new_dish.items():
        if v == 'O':
            new_dish[k] = '.'
    #draw_sketch(new_dish)
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

    for d1 in range(maxs[0 ^ xor] + 1):
        for d2 in range(maxs[1 ^ xor] + 1):
            dirs = [d1, d2]
            dirs = [dirs[0 ^ xor], dirs[1 ^ xor]]
            if reverse:
                dirs[1 ^ xor] = maxs[1 ^ xor] - dirs[1 ^ xor]
            dirs = tuple(dirs)
            v = dish[dirs]
            if v == 'O':
                coord = dirs
                prev_coord = coord
                while coord in new_dish and new_dish[coord] == '.':
                    prev_coord = coord
                    coord = (coord[0] + tilt_dirs[tilt_dir][0], coord[1] + tilt_dirs[tilt_dir][1])
                new_dish[prev_coord] = 'O'
    return new_dish

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