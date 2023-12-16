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

class Beam:
    dirs = {
        'up': (0, -1),
        'down': (0, 1),
        'left': (-1, 0),
        'right': (1, 0)
    }
    def __init__(self, pos, dir, contraption):
        self.pos = pos
        self.dir = dir
        self.contraption = contraption
        self.active = True
    
    def move(self):
        new_beam = None
        next_pos = (self.pos[0] + self.dirs[self.dir][0], self.pos[1] + self.dirs[self.dir][1])
        if next_pos not in self.contraption:
            self.active = False
        else:
            self.pos = next_pos
            match self.contraption[self.pos]:
                case '|':
                    if self.dir == 'left' or self.dir == 'right':
                        self.dir = 'up'
                        new_beam = Beam(self.pos, 'down', self.contraption)
                case '-':
                    if self.dir == 'up' or self.dir == 'down':
                        self.dir = 'left'
                        new_beam = Beam(self.pos, 'right', self.contraption)
                case '/':
                    match self.dir:
                        case 'up':
                            self.dir = 'right'
                        case 'down':
                            self.dir = 'left'
                        case 'left':
                            self.dir = 'down'
                        case 'right':
                            self.dir = 'up'
                case '\\':
                    match self.dir:
                        case 'up':
                            self.dir = 'left'
                        case 'down':
                            self.dir = 'right'
                        case 'left':
                            self.dir = 'up'
                        case 'right':
                            self.dir = 'down'
        return new_beam

def part1(contraption, startpos=(-1, 0), startdir='right'):
    beam = Beam(startpos, startdir, contraption)
    beams = [beam]

    visited = set()
    new_beams = []
    while True:
        active_beams = False
        for beam in beams:
            if beam.active:
                active_beams = True
                new_beam = beam.move()
                if (beam.pos, beam.dir) in visited:
                    beam.active = False
                else:
                    visited.add((beam.pos, beam.dir))
                if new_beam:
                    if (new_beam.pos, new_beam.dir) not in visited:
                        new_beams.append(new_beam)
                        visited.add((new_beam.pos, new_beam.dir))
        beams.extend(new_beams)
        new_beams = []
        if not active_beams:
            break

    return len(set([v[0] for v in visited]))

def part2(contraption):
    max_x = max(contraption, key=lambda x:x[0])[0]
    max_y = max(contraption, key=lambda x:x[1])[1]

    max_energized = 0

    for x in range(max_x + 1):
        max_energized = max(max_energized, part1(contraption, (x, -1), 'down'))
        max_energized = max(max_energized, part1(contraption, (x, max_y + 1), 'up'))
    for y in range(max_y + 1):
        max_energized = max(max_energized, part1(contraption, (-1, y), 'right'))
        max_energized = max(max_energized, part1(contraption, (max_x + 1, y), 'left'))       

    return max_energized

def main():
    contraption = {}
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]
    for y, line in enumerate(input):
        for x, v in enumerate(line):
            contraption[(x, y)] = v
    #draw_sketch(contraption)
    print("Part 1: " + str(part1(contraption)))
    print("Part 2: " + str(part2(contraption)))

if __name__ == "__main__":
    main()