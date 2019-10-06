#!/usr/bin/env python3
import math

N = int(input().split()[0])
a_list = list(map(int, input().split()))

total = sum(a_list)
work_list = []
sunuke = 0

for i in range(N - 1):
    sunuke += a_list[i]
    arai = total - sunuke
    work_list.append(abs(sunuke - arai))

ans = min(work_list)
print(ans)
