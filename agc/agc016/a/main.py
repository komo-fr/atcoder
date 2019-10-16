#!/usr/bin/env python3

s = input()
s_list = list(s)
min_count = float("inf")

for char in set(s_list):
    w_list = s_list[:]
    after_list = []

    count = 0
    while len(set(w_list)) != 1:
        after_list = []
        for i in range(len(w_list) - 1):
            if w_list[i + 1] == char:
                after_list += [char]
            else:
                after_list += w_list[i]
        count += 1
        w_list = after_list

    if count < min_count:
        min_count = count
        ans = "".join(w_list)

ans = min_count
print(ans)
