#!/usr/bin/env python3

n_list = list(map(int, input().split()))
K = int(input().split()[0])

n_list = list(sorted(n_list, reverse=True))
n = n_list[0]
for _ in range(K):
    n = n * 2
ans = n + n_list[1] + n_list[2]
print(ans)
