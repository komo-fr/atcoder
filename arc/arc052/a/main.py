#!/usr/bin/env python3

S = input()
n_list = []
for char in list(S):
    if char in [str(i) for i in range(10)]:
        n_list.append(char)

ans = "".join(n_list)

print(ans)
