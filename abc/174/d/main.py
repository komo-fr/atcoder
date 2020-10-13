#!/usr/bin/env python3

N = int(input().split()[0])
c_input = input()
l_white_count = 0
r_red_count = 0
swap_count = 0


for i in range(N // 2 + 1):
    l = i
    r = (N - 1) - i

    if c_input[l] == "W":
        l_white_count += 1
    if l != r and c_input[r] == "R":
        r_red_count += 1
    if r_red_count > 0 and l_white_count > 0:
        swap_count += 1
        l_white_count -= 1
        r_red_count -= 1

if N % 2 != 0:
    if c_input[N // 2] == "W" and r_red_count > 0:
        swap_count += 1
    elif c_input[N // 2] == "R" and l_white_count > 0:
        swap_count += 1

ans = swap_count
print(ans)
