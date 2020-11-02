#!/usr/bin/env python3

N = int(input().split()[0])
s_table = []

for _ in range(N):
    s = set(list(input()))
    s_table.append(s)

text = ""
found_flag = True
for i in range(N // 2):
    left = s_table[i]
    right = s_table[-(i + 1)]

    common = left & right
    if common:
        text += list(common)[0]
    else:
        found_flag = False
        break

if found_flag:
    if N % 2 == 1:
        text = text + s_table[N // 2][0] + "".join(list(reversed(text)))
    else:
        text += "".join(list(reversed(text)))
    print(text)
else:
    print(-1)
