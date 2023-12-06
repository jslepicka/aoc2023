import os

dirs = {
    "left": (-1, 0),
    "right": (1, 0),
    "up": (0, -1),
    "down": (0, 1),
    "upper-left": (-1, -1),
    "upper-right": (1, -1),
    "lower-left": (-1, 1),
    "lower-right": (1, 1)
}

def part1(input, part_id_locs, part_id_mapping):
    part_numbers = []
    for loc in input:
        val = input[loc]
        if not val.isdigit() and val != '.':
            #this is a part location
            #print(f'{val} at {loc}')
            adjacent_part_ids = set()
            for dir in dirs.values():
                check_loc = (loc[0] + dir[0], loc[1] + dir[1])
                #print(f'checking {check_loc}')
                if check_loc in part_id_locs:
                    part_id = part_id_locs[check_loc]
                    adjacent_part_ids.add(part_id)
                    #print(f'found part_id {part_id} at {check_loc}')
            #print(adjacent_part_ids)
            for a in adjacent_part_ids:
                part_numbers.append(part_id_mapping[a])
    #print(part_numbers)
    return sum(part_numbers)

def part2(input, part_id_locs, part_id_mapping):
    gear_ratios = []
    for loc in input:
        val = input[loc]
        if val == '*':
            #print(f'* at {loc}')
            adjacent_part_ids = set()
            for dir in dirs.values():
                check_loc = (loc[0] + dir[0], loc[1] + dir[1])
                #print(f'checking {check_loc}')
                if check_loc in part_id_locs:
                    part_id = part_id_locs[check_loc]
                    adjacent_part_ids.add(part_id)
                    #print(f'found part_id {part_id} at {check_loc}')
            #print(adjacent_part_ids)
            if (len(adjacent_part_ids) == 2):
                #print(f'gear at {loc}')
                ratio = 1
                for a in adjacent_part_ids:
                    ratio *= part_id_mapping[a]
                gear_ratios.append(ratio)
    #print(gear_ratios)
    return sum(gear_ratios)

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = {}
    part_id_mapping = {}
    part_id_locs = {}

    y = 0
    part_id = 0
    part_number_buf = ""
    with open(day + ".txt") as file:
        while line := file.readline():
            line = line.strip()
            x = 0
            for char in line:
                input[(x, y)] = char
                if char.isdigit():
                    part_id_locs[(x, y)] = part_id
                    part_number_buf += char
                else:
                    if (len(part_number_buf) > 0):
                        #print(part_number_buf)
                        part_id_mapping[part_id] = int(part_number_buf)
                    part_id += 1
                    part_number_buf = ""
                x += 1
            y += 1
    
    print("Part 1: " + str(part1(input, part_id_locs, part_id_mapping)))
    print("Part 2: " + str(part2(input, part_id_locs, part_id_mapping)))

if __name__ == "__main__":
    main()