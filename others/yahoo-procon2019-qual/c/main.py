#!/usr/bin/env python3

K, A, B = list(map(int, input().split()))
if (B - A) <= 2:
    ans = K + 1
else:
    k = K - A + 1
    c = A + (k // 2) * (B - A)
    if k % 2:
        c += 1
    ans = c
print(ans)
