import os
import re

def part1(games):
    max_vals = {'red': 12, 'green': 13, 'blue': 14}
    ret = 0
    for game in games:
        possible = True
        results = games[game]
        for r in results:
            colors = {'red': 0, 'green': 0, 'blue': 0}
            for v, color in r:
                colors[color] += int(v)
            for color in colors:
                if colors[color] > max_vals[color]:
                    possible = False
        if possible:
            ret += game
    return ret

def part2(games):
    ret = 0
    for game in games:
        results = games[game]
        mins = {'red': 0, 'green': 0, 'blue': 0}
        for r in results:
            colors = {'red': 0, 'green': 0, 'blue': 0}
            for v, color in r:
                colors[color] += int(v)
            for color in colors:
                mins[color] = max(mins[color], colors[color])
        power = 1
        for v in mins.values():
            power *= v
        ret += power
    return ret

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]
    games = {}
    for i in input:
        g, results = i.split(':')
        results = results.split(';')
        s = []
        for r in results:
            if m:= re.findall("(\d+) (red|blue|green)", r):
                s.append(m)
        game_number = int(g.split(' ')[1])
        games[game_number] = s
    print("Part 1: " + str(part1(games)))
    print("Part 2: " + str(part2(games)))

if __name__ == "__main__":
    main()