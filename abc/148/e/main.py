#!/usr/bin/env python3

N = int(input().split()[0])

if N % 2 == 0:
    total_n = 0
    count = 1
    while True:
        p = (N // 2) // (5 ** count)
        total_n += p
        count += 1
        if p <= 0:
            break
    ans = total_n
else:
    ans = 0

print(ans)
