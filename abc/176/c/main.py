#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
before_a = 0
total = 0
for i, a in enumerate(a_list):
    if i == 0:
        before_a = a
        continue
    total += max(before_a - a, 0)
    before_a = a + max(before_a - a, 0)
ans = total
print(ans)
