#!/usr/bin/env python3
import math

X = int(input().split()[0])
x = 100
count = 0
while x < X:
    x = int(math.floor(x * 1.01))
    print(f"{count}: {x}")
    count += 1

ans = count
print(ans)
