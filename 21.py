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

dirs = {
    "left": (-1, 0),
    "right": (1, 0),
    "up": (0, -1),
    "down": (0, 1),
}

def bfs(sketch, start_coord, max_depth):
    max_x = max(sketch, key=lambda x:x[0])[0] + 1
    max_y = max(sketch, key=lambda x:x[1])[1] + 1
    next = [start_coord]
    for i in range(max_depth):
        #print(i)
        q = list(next)
        next = set()
        while q:
            coord = q.pop(0)
            for d in dirs:
                next_coord = (coord[0] + dirs[d][0], coord[1] + dirs[d][1])
                if sketch[(next_coord[0] % max_x, next_coord[1] % max_y)] != '#':
                    next.add(next_coord)
    return len(next)

def part1(map, start):
    return bfs(map.copy(), start, 64)

def part2(map, start):
    skip_bfs = False
    if skip_bfs:
        x1 = 65
        x2 = 65 + 131
        x3 = 65 + 131 + 131
        y1 = 3751
        y2 = 33531
        y3 = 92991
    else:
        x1 = 65 # steps to edge of first map
        y1 = bfs(map.copy(), start, x1) 
        x2 = 65 + 131 # steps to edge of second map
        y2 = bfs(map.copy(), start, x2)
        x3 = 65 + 131 + 131 # steps to edge of third map
        y3 = bfs(map.copy(), start, x3)
        #y1=3751, y2=33531, y3=92991

    #lagrange interpolation: https://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html
    lagrange = lambda x: (((x - x2) * (x - x3)) / ((x1 - x2) * (x1 - x3))) * y1 + \
                         (((x - x1) * (x - x3)) / ((x2 - x1) * (x2 - x3))) * y2 + \
                         (((x - x1) * (x - x2)) / ((x3 - x1) * (x3 - x2))) * y3
    
    return int(lagrange(26501365))

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]


    map = {}
    start = None
    for y, line in enumerate(input):
        for x, v in enumerate(line):
            if v == 'S':
                start = (x, y)
                v = '.'
            map[(x, y)] = v
    #draw_sketch(map)

    print("Part 1: " + str(part1(map, start)))
    print("Part 2: " + str(part2(map, start)))

if __name__ == "__main__":
    main()