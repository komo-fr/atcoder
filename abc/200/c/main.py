#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
count = 0
for i in range(N):
    if i == N - 1:
        break
    for j in range(i+1, N):
        a = a_list[i] - a_list[j]
        if a % 200 == 0:
            count += 1
ans = count
print(ans)
