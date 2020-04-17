#!/usr/bin/env python3
import math

N = int(input().split()[0])
X = N / 1.08

if math.floor(math.ceil(X) * 1.08) == N:
    ans = math.ceil(X)
elif math.floor(math.floor(X) * 1.08) == N:
    ans = math.floor(X)
else:
    ans = ":("

print(ans)
