import os

def get_reflections(lines, part2):
    result = 0
    for i, _ in enumerate(lines[:-1]):
        prev = i
        next = i+1
        errors = 0
        while prev >= 0 and next < len(lines):
            a = lines[prev]
            b = lines[next]
            errors += (a ^ b).bit_count()
            prev -= 1
            next += 1
        if (not part2 and errors == 0) or (part2 and errors == 1):
            result += i + 1
            break
    return result    

def part1(input, part2=False):
    left_cols = 0
    up_rows = 0
    
    for i in input:
        up_rows += get_reflections(i['rows'], part2)
        left_cols += get_reflections(i['cols'], part2)

    return left_cols + up_rows * 100

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]

    patterns = []
    pattern = {}

    y = 0
    for line in input:
        x = 0
        if line == '':
            y = 0
            patterns.append(pattern)
            pattern = {}
        else:
            for x, v in enumerate(line):
                pattern[(x, y)] = v
            y += 1
    if len(pattern) > 0:
        patterns.append(pattern)

    rc = []

    for p in patterns:
        cols = []
        rows = []
        pattern_width = max(p, key=lambda x:x[0])[0]
        pattern_height = max(p, key=lambda x:x[1])[1]
        
        for y in range(0, pattern_height+1):
            row = 0
            for x in range(0, pattern_width+1):
                row <<= 1
                if p[(x,y)] == '#':
                    row |= 1
            #print(bin(row))
            rows.append(row)

        for x in range(0, pattern_width + 1):
            col = 0
            for y in range(0, pattern_height + 1):
                col <<= 1
                if p[(x,y)] == '#':
                    col |= 1
            #print(bin(col))
            cols.append(col)
        rc.append({'cols': cols, 'rows': rows})

    print("Part 1: " + str(part1(rc)))
    print("Part 2: " + str(part1(rc, True)))

if __name__ == "__main__":
    main()