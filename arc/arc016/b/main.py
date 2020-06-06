#!/usr/bin/env python3

N = int(input().split()[0])
x_table = []

for _ in range(N):
    x_list = list(input())
    x_table.append(x_list)

x_table = list(zip(*x_table))
count = 0

for x_list in x_table:
    is_on_o = False
    for x in x_list:
        if x == "x":
            count += 1
            is_on_o = False
        elif x == ".":
            is_on_o = False
        else:
            if is_on_o:
                continue
            else:
                is_on_o = True
                count += 1
ans = count

print(ans)
