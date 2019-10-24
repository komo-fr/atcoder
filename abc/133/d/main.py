#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))

r_list = []
total = 0

for i in range(1, N, 2):
    total += a_list[i]

r_list.append(sum(a_list) - total * 2)

for i in range(1, N):
    r = a_list[i - 1] * 2 - r_list[i - 1]
    r_list.append(r)

ans = " ".join([str(w) for w in r_list])
print(ans)
