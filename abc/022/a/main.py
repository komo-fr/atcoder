#!/usr/bin/env python3

N, S, T = list(map(int, input().split()))
W = int(input().split()[0])
a_list = []

for _ in range(N - 1):
    a = int(input())
    a_list.append(a)

w = W
c = 0
for i, a in enumerate(a_list):
    if i != 0:
        work_w = w + a
        w = max(work_w, 1)
    if S <= w <= T:
        c += 1
ans = c
print(ans)
