#!/usr/bin/env python3
from collections import defaultdict

S = input()
pre = ""
post = ""
s_list = []

for i in range(len(S)):
    pre += S[i]
    post = S[i + 1 :]
    s_list.append(post + pre)
s_list = sorted(s_list)

print(s_list[0])
print(s_list[-1])
