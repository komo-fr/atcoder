#!/usr/bin/env python3

N, M, A, B = list(map(int, input().split()))
c_list = []
n = N
for _ in range(M):
    c = int(input().split()[0])
    c_list.append(c)
ans = "complete"
for i, c in enumerate(c_list):
    if n <= A:
        n += B
    n -= c
    if n < 0:
        ans = i + 1
        break

print(ans)
