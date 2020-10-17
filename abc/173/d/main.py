#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
min_a = min(a_list)

ans = min_a * (N - 1)

print(ans)
