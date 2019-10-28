#!/usr/bin/env python3

N = int(input().split()[0])

odd_n = (N + 1) // 2
even_n = N // 2

ans = odd_n * even_n
print(ans)
