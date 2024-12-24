def parse_initial(line):
    line = line.strip()
    a, b = line.split(": ")
    return (a, int(b))

def parse_gate(line):
    line = line.strip()
    [a, b] = line.split(" -> ")
    return (b, a.split())

def read_file(filename):
    with open(filename, 'rt') as f:
        [initial, gates] = f.read().split("\n\n")
        initial = dict([parse_initial(line) for line in initial.splitlines()])
        gates = dict([parse_gate(line) for line in gates.splitlines()])
        return initial, gates

def part1(filename):
    initial, gates = read_file(filename)
    while gates:
        to_delete = []
        for output, [a, operation, b] in gates.items():
            if a in initial and b in initial:
                if operation == "AND":
                    initial[output] = initial[a] & initial[b]
                elif operation == "OR":
                    initial[output] = initial[a] | initial[b]
                elif operation == "XOR":
                    initial[output] = initial[a] ^ initial[b]
                to_delete.append(output)
        for output in to_delete:
            gates.pop(output, None)
    ans = 0
    for k, v in initial.items():
        if k.startswith("z"):
            pos = int(k[1:])
            if v:
                ans |= (1 << pos)
    print(ans)
    return ans


def part2(filename):
    pass

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    # assert 4 == main("example.txt", 1)
    # assert 2024 == main("example2.txt", 1)
    main("2024/24/input.txt", 1)
# 49574189473968
