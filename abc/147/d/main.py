#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
t = 0
mod = 10 ** 9 + 7

for i in range(N - 1):
    for j in range(i + 1, N):
        t += a_list[i] ^ a_list[j]
        t = t % mod
ans = t

print(ans)
