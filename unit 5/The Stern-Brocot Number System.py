import sys

def stern_brocot_path(a, b):
    left, right, mid = (0, 1), (1, 0), (1, 1)
    res = []

    while mid != (a, b):
        v1, v2 = a * mid[1], b * mid[0]
        if v1 < v2:  # go left
            right = mid
            mid = (left[0] + mid[0], left[1] + mid[1])
            res.append('L')
        else:  # go right
            left = mid
            mid = (mid[0] + right[0], mid[1] + right[1])
            res.append('R')

    return ''.join(res)

def main():
    for line in sys.stdin:
        a, b = map(int, line.split())
        if a == 1 and b == 1:
            break
        print(stern_brocot_path(a, b))

if __name__ == "__main__":
    main()
