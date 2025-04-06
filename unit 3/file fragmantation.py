import sys
from collections import defaultdict

def read_input():
    lines = sys.stdin.read().split('\n')
    lines = [line.strip() for line in lines]

    T = 0
    while T < len(lines) and lines[T] == "":
        T += 1

    T = int(lines[T])
    cases = []
    fragments = []

    for line in lines[T+1:]:
        if line == "":
            if fragments:
                cases.append(fragments)
                fragments = []
        else:
            fragments.append(line)

    if fragments:
        cases.append(fragments)

    return T, cases

def solve_case(fragments):
    freq = defaultdict(int)
    n = len(fragments)
    for i in range(n):
        for j in range(n):
            if i != j:
                combined = fragments[i] + fragments[j]
                freq[combined] += 1
    return max(freq.items(), key=lambda x: x[1])[0]

def main():
    T, cases = read_input()

    for i in range(T):
        print(solve_case(cases[i]))
        if i < T - 1:
            print()

if __name__ == "__main__":
    main()
