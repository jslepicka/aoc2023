import os
from itertools import combinations

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

def get_distance(a, b):
    #manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def part1(galaxy_locs, x_expansions, y_expansions, expansion_size=2):
    # for loc in galaxy_locs:
    #     print(f'{loc} {galaxy_locs[loc]}')
    pairs = combinations(galaxy_locs, 2)
    s = 0
    for p in pairs:
        #print(f'checking pair {p}')
        loc1 = galaxy_locs[p[0]]
        loc2 = galaxy_locs[p[1]]
        #print(f'loc1: {loc1} loc2: {loc2}')
        expansion_crossings = 0
        for x in x_expansions:
            if x > min(loc1[0], loc2[0]) and x < max(loc1[0], loc2[0]):
                expansion_crossings += 1
        for y in y_expansions:
            if y > min(loc1[1], loc2[1]) and y < max(loc1[1], loc2[1]):
                expansion_crossings += 1

        distance = get_distance(loc1, loc2)
        distance = distance + expansion_crossings * (expansion_size - 1)
        #print(f'distance between {loc1} and {loc2} is {distance}')
        s += distance

    return s

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    image = {}
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]
    
    galaxy_number = 1
    galaxy_locs = {}
    y_expansions = []
    x_expansions = {}

    for y, line in enumerate(input):
        num_galaxies_this_line = 0
        for x, v in enumerate(line):
            if x not in x_expansions:
                x_expansions[x] = 0
            if v == '#':
                galaxy_locs[galaxy_number] = (x, y)
                galaxy_number += 1
                num_galaxies_this_line += 1
                x_expansions[x] = 1
            image[(x, y)] = v
        if num_galaxies_this_line == 0:
            y_expansions.append(y)

    x_expansions = [k for k, v in x_expansions.items() if v == 0]
    
    #draw_sketch(image)

    print("Part 1: " + str(part1(galaxy_locs, x_expansions, y_expansions)))
    print("Part 2: " + str(part1(galaxy_locs, x_expansions, y_expansions, 1000000)))

if __name__ == "__main__":
    main()