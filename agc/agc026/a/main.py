#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
count = 0
for i in range(1, N):
    if a_list[i-1] == a_list[i]:
        a_list[i] = -1
        count += 1
ans = count
print(ans)
