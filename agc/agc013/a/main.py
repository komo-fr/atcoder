#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))

c = 0
is_minus = True
start_flag = True

for i in range(1, N):
    if start_flag:
        if a_list[i] == a_list[i - 1]:
            continue
        is_minus = True if a_list[i] < a_list[i - 1] else False
        start_flag = False
        continue

    if is_minus:
        if a_list[i] > a_list[i - 1]:
            c += 1
            start_flag = True
    else:
        if a_list[i] < a_list[i - 1]:
            c += 1
            start_flag = True

ans = c + 1
print(ans)
