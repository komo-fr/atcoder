#!/usr/bin/env python3

N, M = list(map(int, input().split()))
if N == 1 and M != 1:
    ans = 1
elif N != 1 and M == 1:
    ans = 1
else:
    a = ((N + 1) // 2) * ((M + 1) // 2)
    b = (N // 2) * (M // 2)
    ans = a + b
print(ans)
