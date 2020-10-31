#!/usr/bin/env python3

N = int(input().split()[0])
D, X = list(map(int, input().split()))
a_list = []

for _ in range(N):
    a = int(input().split()[0])
    a_list.append(a)

count = 0
for a in a_list:
    i = 0
    while a * i + 1 <= D:
        count += 1
        i += 1
ans = count + X
print(ans)
