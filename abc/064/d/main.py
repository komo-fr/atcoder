#!/usr/bin/env python3
import collections

N = int(input().split()[0])
S = input()

ext_n_open, ext_n_close = 0, 0
sub_s = ""

for i, ch in enumerate(list(S)):
    if ch == "(":
        ext_n_open += 1
    else:
        if ext_n_open == 0:
            # 余分な)である
            ext_n_close += 1
        else:
            # 以前出た(と相殺
            ext_n_open -= 1

ans = "(" * ext_n_close + S + ")" * ext_n_open

print(ans)
