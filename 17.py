import os
from heapq import heappop, heappush

def part1(map, part2 = False):
    max_x = max(map, key=lambda x:x[0])[0]
    max_y = max(map, key=lambda x:x[1])[1]
    start = (0, 0, 0, '')
    q = [start]
    cost_so_far = dict()
    cost_so_far[start] = 0

    max_consecutive = 10 if part2 else 3
    min_consecutive = 4 if part2 else 0

    first = True
    while q:
        current = heappop(q)
        x, y, consecutive, dir = current

        next_nodes = []
        if first:
            next_nodes = [(1, 0, 1, 'east'), (0, 1, 1, 'south')]
            first = False
        else:
            match dir:
                case 'north':
                    n = (x, y - 1)
                    if consecutive < max_consecutive and n in map:
                        next_nodes.append((n[0], n[1], consecutive + 1, 'north'))
                    if consecutive >= min_consecutive:
                        n = (x - 1, y)
                        if n in map:
                            next_nodes.append((n[0], n[1], 1, 'west'))
                        n = (x + 1, y)
                        if n in map:
                            next_nodes.append((n[0], n[1], 1, 'east'))
                case 'east':
                    n = (x + 1, y)
                    if consecutive < max_consecutive and n in map:
                        next_nodes.append((n[0], n[1], consecutive + 1, 'east'))
                    if consecutive >= min_consecutive:
                        n = (x, y - 1)
                        if n in map:
                            next_nodes.append((n[0], n[1], 1, 'north'))
                        n = (x, y + 1)
                        if n in map:
                            next_nodes.append((n[0], n[1], 1, 'south'))
                case 'south':
                    n = (x, y + 1)
                    if consecutive < max_consecutive and n in map:
                        next_nodes.append((n[0], n[1], consecutive + 1, 'south'))
                    if consecutive >= min_consecutive:
                        n = (x - 1, y)
                        if n in map:
                            next_nodes.append((n[0], n[1], 1, 'west'))
                        n = (x + 1, y)
                        if n in map:
                            next_nodes.append((n[0], n[1], 1, 'east'))
                case 'west':
                    n = (x - 1, y)
                    if consecutive < max_consecutive and n in map:
                        next_nodes.append((n[0], n[1], consecutive + 1, 'west'))
                    if consecutive >= min_consecutive:
                        n = (x, y - 1)
                        if n in map:
                            next_nodes.append((n[0], n[1], 1, 'north'))
                        n = (x, y + 1)
                        if n in map:
                            next_nodes.append((n[0], n[1], 1, 'south'))
        
        for next in next_nodes:
            new_cost = cost_so_far[current] + map[(next[0], next[1])]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                heappush(q, next)

    return min([v for k, v in cost_so_far.items() if k[0] == max_x and k[1] == max_y])

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]

    map = {}
    for y, line in enumerate(input):
        for x, cost in enumerate(line):
            map[(x, y)] = int(cost)

    print("Part 1: " + str(part1(map)))
    print("Part 2: " + str(part1(map, True)))

if __name__ == "__main__":
    main()