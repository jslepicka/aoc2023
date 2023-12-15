import os
import re

def get_hash(i):
    v = 0
    for c in i:
        v += ord(c)
        v *= 17
        v &= 0xFF
    return v

def part1(input):
    result = 0
    for i in input.split(','):
        result += get_hash(i)
    return result

class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length

def part2(input):
    boxes = {key: [] for key in range(256)}
    for i in input.split(','):
        label, op, focal_length = re.split(r'(=|-)', i)
        box_number = get_hash(label)
        if op == '-':
            for x, lens in enumerate(boxes[box_number]):
                if lens.label == label:
                    del boxes[box_number][x]
                    break
        elif op == '=':
            new_lens = Lens(label, int(focal_length))
            replaced_lens = False
            for x, lens in enumerate(boxes[box_number]):
                if lens.label == label:
                    boxes[box_number][x] = new_lens
                    replaced_lens = True
                    break
            if not replaced_lens:
                boxes[box_number].append(new_lens)

    focusing_power = 0
    for box_number in range(256):
        for i, lens in enumerate(boxes[box_number]):
            fp = (box_number + 1) * (i + 1) * lens.focal_length
            focusing_power += fp
    return focusing_power

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = ""
    with open(day + ".txt") as file:
        input = file.readline().strip()
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()