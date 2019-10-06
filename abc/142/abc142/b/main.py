#!/usr/bin/env python3

N, K = list(map(int, input().split()))
h_list = list(map(int, input().split()))
ans = len([h for h in h_list if h >= K])

print(ans)
