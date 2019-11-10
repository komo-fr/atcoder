#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))

odd_n = 0
even_n = 0

for a in a_list:
    if a % 2 == 1:
        odd_n += 1
    else:
        even_n += 1

ans = "YES" if odd_n % 2 == 0 else "NO"

print(ans)
