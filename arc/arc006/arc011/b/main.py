#!/usr/bin/env python3
import collections

N = int(input().split()[0])
w_list = list(input().split())

str2number_map = collections.defaultdict(lambda: "")
str2number_list = "zr,bc,dw,tj,fq,lv,sx,pm,hk,ng".split(",")
for i, s in enumerate(str2number_list):
    for char in s:
        str2number_map[char] = i
after_list = []
for w in w_list:
    after = ""
    for char in w.lower():
        after += str(str2number_map[char])
    if after:
        after_list.append(after)
ans = " ".join(after_list)

print(ans)
