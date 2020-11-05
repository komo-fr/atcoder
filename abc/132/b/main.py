#!/usr/bin/env python3

n = int(input().split()[0])
p_list = list(map(int, input().split()))
count = 0

for i in range(1, n - 1):
    a, b, c = p_list[i - 1], p_list[i], p_list[i + 1]
    if a <= b <= c or c <= b <= a:
        count += 1

ans = count
print(ans)
