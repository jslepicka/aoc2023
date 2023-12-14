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

    def get_cols(rows):
        cols = []
        for x, _ in enumerate(rows[0]):
            v = ""
            for y, _ in enumerate(rows):
                v += rows[y][x]
            cols.append(v)
        return cols

    rc = []
    rows = []
    input_len = len(input)
    for i, line in enumerate(input):
        if line == '' or i == input_len - 1:
            if len(rows) > 0:
                r = [int(x, 2) for x in rows]
                c = [int(x, 2) for x in get_cols(rows)]
                rc.append({'rows': r, 'cols': c})
            rows = []
        else:
            n = line.replace('#', '1').replace('.', '0')
            rows.append(n)

    print("Part 1: " + str(part1(rc)))
    print("Part 2: " + str(part1(rc, True)))

if __name__ == "__main__":
    main()