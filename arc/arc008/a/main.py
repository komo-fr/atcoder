#!/usr/bin/env python3

N = int(input().split()[0])

a_1 = (N // 10) * 100 + (N % 10) * 15
a_2 = ((N // 10) + 1) * 100
ans = min(a_1, a_2)

print(ans)
