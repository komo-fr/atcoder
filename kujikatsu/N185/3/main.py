#!/usr/bin/env python3

N = int(input().split()[0])
c_list = list(input())

l_white_c = 0
r_red_c = 0
count = 0

total_r = 0
total_w = 0
for i in range(N // 2):
    # print(f"{i=}")
    j = N - (i + 1)

    left = c_list[i]
    right = c_list[j]

    if left == "W":
        total_w += 1
    else:
        total_r += 1
    if right == "W":
        total_w += 1
    else:
        total_r += 1

    if left == "W":
        l_white_c += 1
    if right == "R":
        r_red_c += 1
    if l_white_c > 0 and r_red_c > 0:
        l_white_c -= 1
        r_red_c -= 1
        count += 1
else:
    if N % 2 != 0:
        c = c_list[N // 2]
        # print(f"{c=}")
        if c == "W":
            total_w += 1
        else:
            total_r += 1
        if c == "W" and r_red_c > 0:
            r_red_c -= 1
            count += 1
        elif c == "R" and l_white_c > 0:
            l_white_c -= 1
            count += 1

# print(f"{l_white_c=}, {r_red_c=}")

if total_w == 0 or total_r == 0:
    count = 0
elif l_white_c != 0 and r_red_c != 0:
    count += min([l_white_c, r_red_c])

ans = count
print(ans)
