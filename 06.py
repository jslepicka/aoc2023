import os
from math import ceil, floor

def solve(time, distance):
    # x(t-x) > d
    # for time = 7, distance = 9
    # x(7-x) > 9
    # 7x - x**2 > 9
    # 7x - x**2 - 9 > 0
    # solve using quadratic equation
    a = -1
    b = time
    c = -distance
    delta = b**2 - 4*a*c
    if delta > 0:
        root1 = (-b + delta**.5) / (2 * a)
        root1 = floor(root1) + 1
        root2 = (-b - delta**.5) / (2 * a)
        root2 = ceil(root2) - 1
        #print(f'x1: {x1} x2: {x2}')
        return range(root1, root2+1)
    elif delta == 0:
        #tie
        return None
    else:
        return None

def part1(times, distances):
    result = 1
    for i, t in enumerate(times):
        d = distances[i]
        #print(f't: {t} d: {d}')
        if r := solve(t,d):
            result *= len(r)
    return result

def part2(times, distances):
    new_t = int(''.join([str(x) for x in times]))
    new_d = int(''.join([str(x) for x in distances]))
    #print(f'{new_t} {new_d}')
    r = solve(new_t, new_d)
    return len(r)

def main():
    day=os.path.abspath(__file__).split('.')[0]
    times = []
    distances = []
    with open(day + ".txt") as file:
        times = [int(x) for x in file.readline().strip().split(':')[1].split()]
        distances = [int(x) for x in file.readline().strip().split(':')[1].split()]

    print("Part 1: " + str(part1(times, distances)))
    print("Part 2: " + str(part2(times, distances)))
if __name__ == "__main__":
    main()