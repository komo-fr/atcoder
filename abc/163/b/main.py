#!/usr/bin/env python3

N, M = list(map(int, input().split()))
a_list = list(map(int, input().split()))

ans = N - sum(a_list) if N >= sum(a_list) else -1

print(ans)
