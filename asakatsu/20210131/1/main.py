#!/usr/bin/env python3
import math

H = int(input().split()[0])
W = int(input().split()[0])
N = int(input().split()[0])

ans = int(math.ceil(N / max([H, W])))

print(ans)
