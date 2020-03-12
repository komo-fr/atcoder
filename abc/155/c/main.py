#!/usr/bin/env python3

N = int(input().split()[0])
c_list = []
c_dict = {}
cc_dict = {}
max_v = -float("inf")

for _ in range(N):
    c = input()
    c_list.append(c)
    if c in c_dict:
        v = c_dict[c] + 1
        c_dict[c] = v
    else:
        v = 0
        c_dict[c] = 0
        # cc_dict[0] = c
    if v in cc_dict:
        cc_dict[v].append(c)
    else:
        cc_dict[v] = [c]

    if max_v < v:
        max_v = v

k_list = cc_dict[max_v]
k_list = list(sorted(k_list))
ans = "\n".join(k_list)

print(ans)
