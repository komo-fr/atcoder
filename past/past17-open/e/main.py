#!/usr/bin/env python3

S = input()
pre_char = None
count = 0
x_list = []
for i, s in enumerate(S):
    if s != pre_char:
        x_list.append((s, 1))
    else:
        x_list[-1] = (x_list[-1][0], x_list[-1][1] + 1)

    pre_char = s

ans = " ".join([f"{x[0]} {x[1]}" for x in x_list])

print(ans)
