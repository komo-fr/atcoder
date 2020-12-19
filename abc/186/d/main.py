#!/usr/bin/env python3
import numpy as np

N = int(input().split()[0])
a_list = list(map(int, input().split()))
a_list = list(range(2 * 10 ** 5))
total = 0
a_array = np.array(a_list)
for i, a in enumerate(a_list):
    # print(f"{i=}, {a - a_array}")
    total += np.abs(a - a_array).sum()

ans = total // 2
print(ans)
