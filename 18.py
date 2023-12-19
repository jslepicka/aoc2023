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

def flood_fill(sketch, start_coord):
    dirs = {
        "left": (-1, 0),
        "right": (1, 0),
        "up": (0, -1),
        "down": (0, 1),
    }
    stack = []
    visited = {}
    stack.append(start_coord)
    while stack:
        coord = stack.pop()
        if coord in visited:
            continue
        visited[coord] = 1
        sketch[coord] = '#'
        for d in dirs:
            next_coord = (coord[0] + dirs[d][0], coord[1] + dirs[d][1])
            if sketch.get(next_coord, ' ') == ' ':
                stack.append(next_coord)

def part1(plan):
    flood_start = None
    min_x = min(plan, key=lambda x:x[0])[0]
    min_y = min(plan, key=lambda x:x[1])[1]
    max_x = max(plan, key=lambda x:x[0])[0]
    max_y = max(plan, key=lambda x:x[1])[1]
    found = False
    for y in range(min_y, max_y + 1):
        if found:
            break
        for x in range(min_x, max_x + 1):
            v = plan.get((x, y), ' ')
            l = plan.get((x - 1, y), ' ')
            r = plan.get((x + 1, y), ' ')
            if v == '#' and l == ' ' and r == ' ':
                plan[(x + 1), y] = 'F'
                found = True
                flood_start = (x + 1, y)
                break
    #print(f'starting flood fill at {flood_start}')
    flood_fill(plan, flood_start)
    #draw_sketch(plan)
    return len([v for k, v in plan.items() if v != ' '])

def part2(plan, perimeter_len):
    #needed reddit help for this.
    
    #shoelace algorithm (trapezoid formula) to get inside area of polygon
    a = 0
    for i in range(len(plan) - 1):
        a += (plan[i][1] + plan[i + 1][1]) * (plan[i + 1][0] - plan[i][0]) / 2.0
    a = abs(a)

    #picks theorem to get area of simple polygon
    #i is interior points, which we can't directly measure (too large of a search space)
    #we have a from above, so we rearrage
    #a = i + b/2 - 1
    #i = a - b/2 + 1
    #now add in the border
    #i = a - b/2 + 1 + b = a + b/2 + 1
    return int(a + perimeter_len/2 + 1)

def main():
    plan = {}
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]
    dirs = {
        'R': (1, 0),
        'D': (0, 1),
        'L': (-1, 0),
        'U': (0, -1)
    }
    x = 0
    y = 0
    plan[(x, y)] = '#'
    for i in input:
        dir, steps, color = i.split()
        for s in range(int(steps)):
            x += dirs[dir][0]
            y += dirs[dir][1]
            plan[(x, y)] = '#'

    plan2 = [(0, 0)]
    x = 0
    y = 0
    s = 0
    for i in input:
        _, _, ins = i.split()
        ins = ins.replace('(', '').replace(')', '').replace('#', '')
        ins = int(ins, 16)
        dir = ins & 0xF
        dir = ['R', 'D', 'L', 'U'][dir]
        steps = ins >> 4
        s += int(steps)
        x += dirs[dir][0] * int(steps)
        y += dirs[dir][1] * int(steps)
        plan2.append((x, y))

    print("Part 1: " + str(part1(plan.copy())))
    print("Part 2: " + str(part2(plan2, s)))

if __name__ == "__main__":
    main()