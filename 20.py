import os
from math import lcm

class Component:
    def __init__(self):
        self.type = 'Unknown'
        self.inputs = {}
        self.prev_inputs = {}
        self.outputs = set()
        self.output = 'L'
        self.name = ''
    def set_type(self, type):
        match type:
            case 'broadcaster':
                self.type = 'broadcaster'
            case 'flipflop':
                self.type = 'flipflop'
                self.output = 'L'
            case 'conjunction':
                self.type = 'conjunction'
                self.output = 'H'
            case _:
                print('f')
                exit()
    def clock(self, level, source, part2 = False):
        output = True
        match self.type:
            case 'broadcaster':
                self.output = level
            case 'flipflop':
                if level == 'L':
                    self.output = 'H' if self.output == 'L' else 'L'
                else:
                    output = False
            case 'conjunction':
                self.inputs[source] = level
                self.output = 'L'
                for i in self.inputs:
                    if self.inputs[i] == 'L':
                        self.output = 'H'
                        break
        high = False
        if self.type == 'conjunction':
            if self.name in ['vc', 'ls', 'nb', 'vg'] and self.output == 'H':
                high = True
        r = {}
        if output:
            for o in self.outputs:
                r[o] = (self.name, self.output)
        if part2:
            return r, high
        else:
            return r

def part1(components):
    low_count = 0
    high_count = 0
    for _ in range(1000):
        q = []
        q.append({'broadcaster': ('button', 'L')})
        low_count += 1
        while q:
            s = q.pop(0)
            for c in s:
                r = components[c].clock(s[c][1], s[c][0])
                for x in r:
                    q.append({x: r[x]})
                    if r[x][1] == 'L':
                        low_count += 1
                    else:
                        high_count += 1

    #print(f'{low_count} {high_count}')
    return low_count * high_count

def part2(components):
    #drew graph to determine structure
    #if all of these predecessors of rx are outputing H, then rx will receive L
    #find cycle length then return lcm
    cycles = {
        'vc': [None, None],
        'ls': [None, None],
        'nb': [None, None],
        'vg': [None, None]
    }
    press = 0
    while True:
        press += 1
        r = {'broadcaster': ('button', 'L')}
        q = []
        q.append(r)
        while q:
            s = q.pop(0)
            for c in s:
                r, high = components[c].clock(s[c][1], s[c][0], True)
                if high:
                    if cycles[c][0] == None:
                        cycles[c][0] = press
                    elif cycles[c][1] == None:
                        cycles[c][1] = press
                    if all([v[1] != None for v in cycles.values()]):
                        return lcm(*[v[1] - v[0] for v in cycles.values()])
                for x in r:
                    q.append({x: r[x]})

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]

    components = {}
    for i in input:
        i = i.replace('-', '')
        source, dest = i.replace('-', '').split('>')
        source = source.strip()
        dest = dest.replace(',', '').split()
        for d in dest:
            s = source[1:] if '%' in source or '&' in source else source
            if d not in components:
                components[d] = Component()
            components[d].inputs[s] = 'L'
            components[d].name = d
        if source == 'broadcaster':
            type = 'broadcaster'
        elif '%' in source:
            type = 'flipflop'
            source = source[1:]
        elif '&' in source:
            type = 'conjunction'
            source = source[1:]
        if source not in components:
            components[source] = Component()
        for d in dest:
            components[source].outputs.add(d)
        components[source].set_type(type)
        components[source].name = source
            
    print("Part 1: " + str(part1(components)))
    print("Part 2: " + str(part2(components)))

if __name__ == "__main__":
    main()