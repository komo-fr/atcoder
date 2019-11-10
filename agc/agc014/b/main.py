#!/usr/bin/env python3

N = int(input().split()[0])
N, M = list(map(int, input().split()))
ab_list = []

for _ in range(M):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))

print(ans)
