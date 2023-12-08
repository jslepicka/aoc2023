import os
from functools import cache
from math import lcm

def part1(nodes, directions, start_node="AAA", part2=False):
    steps = 0
    input_dirs = directions
    node = start_node
    while True:
        #print(steps)
        dirs = list(input_dirs)
        while len(dirs) > 0:
            if (not part2 and node == 'ZZZ') or (part2 and node[2] == 'Z'):
                return steps
            steps += 1
            d = dirs.pop(0)
            #print(f'on node {node}, moving {d}')
            next_node = nodes[node][0 if d == 'L' else 1]
            node = next_node

def part2(nodes, directions):
    a_nodes = [x for x in nodes.keys() if x[2] == 'A']
    steps = []
    for node in a_nodes:
        s = part1(nodes, directions, node, True)
        steps.append(s)
    return lcm(*steps)

def main():
    day=os.path.abspath(__file__).split('.')[0]
    nodes = {}
    with open(day + ".txt") as file:
        directions = file.readline().strip()
        file.readline()
        for i in [x.strip() for x in file.readlines()]:
            node, paths = i.split('=')
            node = node.strip()
            paths = [x.strip() for x in paths.replace('(', '').replace(')', '').split(',')]
            nodes[node] = paths

    print("Part 1: " + str(part1(nodes, directions)))
    print("Part 2: " + str(part2(nodes, directions)))

if __name__ == "__main__":
    main()