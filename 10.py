import os

dirs = {
    "left": (-1, 0),
    "right": (1, 0),
    "up": (0, -1),
    "down": (0, 1),
}

valid_dirs = {
    "S": ['left', 'right', 'up', 'down'],
    "-": ['left', 'right'],
    '|': ['up', 'down'],
    'L': ['up', 'right'],
    'F': ['down', 'right'],
    'J': ['up', 'left'],
    '7': ['down', 'left']
}

valid_pipes = {
    "left": "-LF",
    "right": "-J7",
    "up": "|7F",
    "down": "|LJ"
}

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


def part1(sketch, input):
    #find first adjacent pipe
    visited = {}
    distance = 0
    my_pos = input
    while True:
        visited[my_pos] = sketch[my_pos]
        #print(f'current position {my_pos}: {sketch[my_pos]}')
        for d in dirs:
            if d not in valid_dirs[sketch[my_pos]]:
                continue
            next_pos = (my_pos[0] + dirs[d][0], my_pos[1] + dirs[d][1])
            if next_pos in sketch:
                if distance > 1 and sketch[next_pos] == 'S':
                    #draw_sketch(visited)
                    return (distance + 1) // 2, visited
                if next_pos not in visited:
                    if sketch[next_pos] in valid_pipes[d]:
                        #print(f"moving {d} to {next_pos}")
                        my_pos = next_pos
                        distance += 1
                        break
    
    return None

def dfs(sketch, start_coord):
    stack = []
    visited = {}
    stack.append(start_coord)
    while stack:
        coord = stack.pop()
        if coord in visited:
            continue
        visited[coord] = 1
        sketch[coord] = 'O'
        for d in dirs:
            next_coord = (coord[0] + dirs[d][0], coord[1] + dirs[d][1])
            if next_coord in sketch and sketch[next_coord] in '. ':
                stack.append(next_coord)

def part2(sketch):
    #passed in sketch is the visited path from part1 (so it doesn't contain empty spaces or pipes we don't care about)
    #draw_sketch(sketch)
    new_sketch = {}

    #expand the sketch adding ' ' if space in between coordinates is passable, 'X' if not
    # S------7     SX-X-X-X-X-X-X7
    # |F----7|     X             X
    # ||    ||     | FX-X-X-X-X7 |
    # ||    || --> X X         X X
    # |L-7F-J|     | |         | |
    # |  ||  |     X X         X X
    # L--JL--J     | |         | |
    #              X X         X X
    #              | LX-X7 FX-XJ |
    #              X     X X     X
    #              |     | |     |
    #              X     X X     X
    #              LX-X-XJ LX-X-XJ
            
    for coord in sketch:
        new_pos = (coord[0] * 2, coord[1] * 2)
        new_sketch[new_pos] = sketch[coord]
        right = (coord[0] + 1, coord[1])
        if sketch[coord] in 'S-LF' and (right in sketch and sketch[right] in 'S-J7'):
            new_sketch[(new_pos[0] + 1, new_pos[1])] = 'X'
        else:
            new_sketch[(new_pos[0] + 1, new_pos[1])] = ' '
        down = (coord[0], coord[1] + 1)
        if sketch[coord] in 'S|7F' and (down in sketch and sketch[down] in 'S|LJ'):
            new_sketch[(new_pos[0], new_pos[1] + 1)] = 'X'
        else:
            new_sketch[(new_pos[0], new_pos[1] + 1)] = ' '
    
    #fill in all of the missing coordinates with ' '
    max_x = max(new_sketch, key=lambda x:x[0])[0]
    max_y = max(new_sketch, key=lambda x:x[1])[1]
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) not in new_sketch:
                new_sketch[(x, y)] = ' '

    #add an empty border around the new sketch
    # .................
    # .SX-X-X-X-X-X-X7.
    # .X             X.
    # .| FX-X-X-X-X7 |.
    # .X X         X X.
    # .| |         | |.
    # .X X         X X.
    # .| |         | |.
    # .X X         X X.
    # .| LX-X7 FX-XJ |.
    # .X     X X     X.
    # .|     | |     |.
    # .X     X X     X.
    # .LX-X-XJ LX-X-XJ.
    # .................

    for x in range(max_x + 1):
        new_sketch[(x, -1)] = '.'
        new_sketch[(x, max_y)] = '.'
    for y in range(-1, max_y + 1):
        new_sketch[(-1, y)] = '.'
        new_sketch[(max_x, y)] = '.'
    #draw_sketch(new_sketch)

    #flood fill from the upper left corner, replacing reachable spots with 'O'
    # OOOOOOOOOOOOOOOOO
    # OSX-X-X-X-X-X-X7O
    # OX             XO
    # O| FX-X-X-X-X7 |O
    # OX XOOOOOOOOOX XO
    # O| |OOOOOOOOO| |O
    # OX XOOOOOOOOOX XO
    # O| |OOOOOOOOO| |O
    # OX XOOOOOOOOOX XO
    # O| LX-X7OFX-XJ |O
    # OX     XOX     XO
    # O|     |O|     |O
    # OX     XOX     XO
    # OLX-X-XJOLX-X-XJO
    # OOOOOOOOOOOOOOOOO
    dfs(new_sketch, (-1, -1))
    #draw_sketch(new_sketch)
    
    #count the number of spaces left, skiping over the rows/columns we added in the first step
    # S------7
    # |F----7|
    # ||OOOO||
    # ||OOOO||
    # |L-7F-J|
    # |  ||  |
    # L--JL--J
    enclosed_tiles = 0
    for y in range(0, max_y + 1, 2):
        for x in range(0, max_x + 1, 2):
            v = new_sketch[(x, y)]
            #print(v, end='')
            if v == ' ':
                enclosed_tiles += 1
        #print()
    return enclosed_tiles

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    sketch = {}
    
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]

    for y, line in enumerate(input):
        for x, v in enumerate(line):
            sketch[(x, y)] = v
            if v == 'S':
                input = (x,y)
    
    #draw_sketch(sketch)
    p1_result, p1_visited = part1(sketch, input)
    print("Part 1: " + str(p1_result))
    print("Part 2: " + str(part2(p1_visited)))

if __name__ == "__main__":
    main()