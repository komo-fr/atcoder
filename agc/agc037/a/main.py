#!/usr/bin/env python3

S = input()
s_list = []
now_s = ""
for i, char in enumerate(reversed(list(S))):
    if now_s + char not in s_list:
        now_s += char
        s_list.append(now_s)
        now_s = ""
    else:
        now_s += char

ans = len(s_list)
print(ans)
