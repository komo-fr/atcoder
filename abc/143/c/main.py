#!/usr/bin/env python3

N = int(input().split()[0])
S = input()
s_list = list(S)
count = 1

for i in range(1, N):
    if s_list[i] != s_list[i - 1]:
        count += 1
ans = count
print(ans)
