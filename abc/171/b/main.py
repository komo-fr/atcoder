#!/usr/bin/env python3

N, K = list(map(int, input().split()))
p_list = list(map(int, input().split()))

ans = sum(sorted(p_list)[:K])

print(ans)
