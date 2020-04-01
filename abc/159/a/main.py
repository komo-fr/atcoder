#!/usr/bin/env python3
import math

N, M = list(map(int, input().split()))

# 偶数だけ
# 奇数だけ


def C(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


t = 0
if N >= 2:
    t += C(N, 2)
if M >= 2:
    t += C(M, 2)
ans = t
print(ans)
