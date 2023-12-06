import os
import re
def part1(input):
    ret = 0
    for i in input:
        x = list([n for n in i if n.isdigit()])
        value = int(x[0] + x[-1])
        ret += value
    return ret

def part2(input):
    nums = {
        'one':   '1',
        'two':   '2',
        'three': '3',
        'four':  '4',
        'five':  '5',
        'six':   '6',
        'seven': '7',
        'eight': '8',
        'nine':  '9'
    }
    ret = 0
    pattern=r'(?=(' + ''.join([k + '|' for k in nums.keys()]) + r'\d))'
    for i in input:
        if m := re.findall(pattern, i):
            x = [m[0], m[-1]]
            v = list(map(lambda x: nums[x] if x in nums else x, x))
            value = int(v[0] + v[1])
            ret += value
    return ret

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()