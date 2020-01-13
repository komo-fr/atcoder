#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))
total = sum(a_list)
if total % N == 0:
    x = total // N
    c = 0
    for i, a in enumerate(a_list):
        if i == N - 1:
            break
        if a > x:
            # 余分な人を右に移す
            a_list[i] = x
            a_list[i + 1] = a_list[i + 1] + (a - x)
            c += 1
        elif a < x:
            # 余分な人を右から移す
            a_list[i] = x
            a_list[i + 1] = a_list[i + 1] - (x - a)
            c += 1
    ans = c
else:
    ans = -1

print(ans)
