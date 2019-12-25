#!/usr/bin/env python3

S = input().split()[0]
N = int(input().split()[0])

s = S
for _ in range(N):
    l, r = list(map(int, input().split()))
    l, r = l - 1, r - 1
    s = s[:l] + "".join(list(reversed(s[l : r + 1]))) + s[r + 1 :]
ans = s
print(ans)
