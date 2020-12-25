#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
ans = sum(a_list) - N
print(ans)
