#!/usr/bin/env python3
from collections import defaultdict

N = int(input().split()[0])
S = input()

patterns = [str(x).zfill(3) for x in range(1000)]
# done_dict = defaultdict(lambda: False)
# done_numbers = []
count = 0
for p in patterns:
    p0, p1, p2 = list(p)
    p0_flag = False
    p1_flag = False
    for char in S:
        if char == p0 and p0_flag is False:
            p0_flag = True
        elif p0_flag and p1_flag is False and char == p1:
            p1_flag = True
        elif p0_flag and p1_flag and char == p2:
            count += 1
            break

ans = count
print(ans)
