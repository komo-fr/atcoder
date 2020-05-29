#!/usr/bin/env python3
import itertools

N, K = list(map(int, input().split()))
s_list = []

for _ in range(K):
    _ = input()
    a_list = list(map(int, input().split()))
    s_list.append(a_list)

s_list = set(itertools.chain.from_iterable(s_list))
ans = N - len(s_list)

print(ans)
