#!/usr/bin/env python3
from collections import defaultdict
import math
N = int(input().split()[0])
a_list = list(map(int, input().split()))

count_dict = defaultdict(lambda: 0)
for a in a_list:
    count_dict[a % 200] += 1

def C(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

count = 0
for v in count_dict.values():
    if v >= 2:
        count += C(v, 2)

ans = count
print(ans)
