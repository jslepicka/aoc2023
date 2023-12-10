import os

def part1(input):
    vals = []
    for j in input:
        last_number = j[-1]
        next = []
        last = []
        while True:
            for i in range(len(j)-1):
                next.append(j[i+1] - j[i])
            last.append(next[-1])
            if all([x == 0 for x in next]):
                vals.append(sum(last) + last_number)
                last = []
                break
            else:
                j = next
                next = []
    return sum(vals)

def part2(input):
    vals = []
    for j in input:
        first_number = j[0]
        next = []
        first = []
        while True:
            for i in range(len(j)-1):
                next.append(j[i+1] - j[i])
            first.append(next[0])
            if all([x == 0 for x in next]):
                result = 0
                for x in reversed(first):
                    result = x - result
                vals.append(first_number - result)
                first = []
                break
            else:
                j = next
                next = []
    return sum(vals)

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        for line in [x.strip() for x in file.readlines()]:
            input.append([int(x) for x in line.split()])
    #print(input)
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()