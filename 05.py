import os

def part1(seeds, maps):
    locations = []
    for seed in seeds:
        #print(seed)
        for map in maps:
            #print(map)
            for e in maps[map]:
                #print(e)
                if seed >= e['start'] and seed < e['start'] + e['len']:
                    seed = e['dest'] + seed - e['start']
                    break
            #print(f' translated to {seed}')
        locations.append(seed)
        #print(f'!!final location {seed}')
    return min(locations)
    
def map_seeds(seed, map, offset):
    passed = []
    mapped = []
    if seed[0] <= map[1] and map[0] <= seed[1]:
        if map[0] <= seed[0] and map[1] >= seed[1]:
            mapped.append([seed[0] + offset, seed[1] + offset])
        elif map[0] <= seed[0]:
            mapped.append([seed[0] + offset, map[1] + offset])
            passed.append([map[1] + 1, seed[1]])
        elif map[1] >= seed[1]:
            mapped.append([map[0] + offset, seed[1] + offset])
            passed.append([seed[0], map[0] - 1])
        else:
            mapped.append([map[0] + offset, map[1] + offset])
            passed.append([seed[0], map[0] - 1])
            passed.append([map[1] + 1, seed[1]])
    else:
        passed.append(seed)
    return mapped, passed

def part2(seeds, maps):
    seed_ranges = []
    for i in range(len(seeds)//2):
        start = seeds[i*2]
        end = seeds[i*2] + seeds[i*2+1] - 1
        seed_ranges.append([start, end])
    for map in maps:
        mapped = []
        for e in maps[map]:
            map_range = [e['start'], e['start'] + e['len'] - 1]
            offset = e['dest'] - e['start']
            passed = []
            for seed in seed_ranges:
                _mapped, _passed = map_seeds(seed, map_range, offset)
                passed.extend(_passed)
                mapped.extend(_mapped)
            seed_ranges = passed
        seed_ranges.extend(mapped)
            
    #print(seed_ranges)
    return min(x[0] for x in seed_ranges)

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]

    seeds = []
    maps = {}
    map_key = ''
    for i in input:
        if i.startswith('seeds:'):
            seeds = [int(x) for x in i.split(':')[1].split()]
        elif i.endswith(':'):
            map_key = i.split()[0]
        elif i != "":
            if (map_key not in maps):
                maps[map_key] = []
            dest, start, len = i.split()
            entry = {
                'dest': int(dest),
                'start': int(start),
                'len': int(len)
            }
            maps[map_key].append(entry)

    print("Part 1: " + str(part1(seeds, maps)))
    print("Part 2: " + str(part2(seeds, maps)))

if __name__ == "__main__":
    main()