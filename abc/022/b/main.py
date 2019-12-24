#!/usr/bin/env python3

N = int(input().split()[0])
a_list = []
for _ in range(N):
    a = int(input().split()[0])
    a_list.append(a)
ans = N - len(set(a_list))
print(ans)
