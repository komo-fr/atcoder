#!/usr/bin/env python3
import math

N = int(input().split()[0])
s = ""

for i in range(math.ceil(math.log2(10 ** 10)) + 1):
    s = str(N % 2) + s
    N = -(N // 2)

ans = s.lstrip("0")
ans = "0" if ans == "" else ans
print(ans)
