import math
import sys

for line in sys.stdin:
    s = line.strip()
    if not s:
        continue
    a = float(s)
    length = len(s) + 1

    while True:
        left = math.log(a, 2) + length * math.log(10, 2)
        right = math.log(a + 1, 2) + length * math.log(10, 2)
        if int(left) < int(right):
            break
        length += 1

    ans = math.ceil(left)
    print(ans)
