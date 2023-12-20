import os

def part1(workflows, parts):
    ratings = 0
    for p in parts:
        wf = 'in'
        x = p['x']
        m = p['m']
        a = p['a']
        s = p['s']
        made_decision = False
        while not made_decision:
            for step in workflows[wf]:
                #print(step)
                result = eval(step[0])
                if result:
                    if step[1] == 'A':
                        made_decision = True
                        ratings += x + m + a + s
                        break
                    elif step[1] == 'R':
                        made_decision = True
                        break
                    else:
                        wf = step[1]
                        break
    return ratings

def part2(workflows):
    x = (1,4000)
    m = (1,4000)
    a = (1,4000)
    s = (1,4000)
    ret = 0
    stack = [('in', 0, x, m, a, s)]
    while stack:
        workflow, step, x, m, a, s = stack.pop()
        if workflow == 'A':
            ret += (x[1] - x[0] + 1) * (m[1] - m[0] + 1) * (a[1] - a[0] + 1) * (s[1] - s[0] + 1)
            continue
        elif workflow == 'R':
            continue
        ins, dest = workflows[workflow][step]
        ranges = {'x': x, 'm': m, 'a': a, 's': s}
        true_ranges = ranges.copy()
        false_ranges = ranges.copy()
        if ins == 'True':
            stack.append((dest, 0, x, m, a, s))
        else:
            if '<' in ins:
                var, v = ins.split('<')
                true_ranges[var] = (ranges[var][0], int(v) - 1)
                false_ranges[var] = (int(v), ranges[var][1])
            elif '>' in ins:
                var, v = ins.split('>')
                true_ranges[var] = (int(v) + 1, ranges[var][1])
                false_ranges[var] = (ranges[var][0], int(v))
            stack.append((dest, 0, *true_ranges.values()))
            stack.append((workflow, step + 1, *false_ranges.values()))
    return ret

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]

    workflows = {}
    parts = []
    in_parts = False
    for i in input:
        if i == '':
            in_parts = True
            continue
        if not in_parts:
            workflow_id, instructions = i.split('{')
            instructions = instructions.replace('}', '')
            workflows[workflow_id] = []
            for ins in instructions.split(','):
                if ':' in ins:
                    comparison, dest = ins.split(':')
                    workflows[workflow_id].append((comparison, dest))
                else:
                    workflows[workflow_id].append(('True', ins))
        else:
            i = i.replace('{', '').replace('}', '')
            x = {}
            for p in i.split(','):
                var, value = p.split("=")
                x[var] = int(value)
            parts.append(x)
    #print(workflows)
    print("Part 1: " + str(part1(workflows, parts)))
    print("Part 2: " + str(part2(workflows)))

if __name__ == "__main__":
    main()