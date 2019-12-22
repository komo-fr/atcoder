#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
x_list = []
max_a = 0
for i in range(N):
    a = a_list[i]
    if a == max_a + 1:
        max_a += 1
ans = N - max_a if max_a != 0 else -1
print(ans)
