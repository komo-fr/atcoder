#!/usr/bin/env python3

s = int(input().split()[0])
s_list = []
n = 1
a = s
i = 2
s_list.append(a)

while True:
    a = a // 2 if a % 2 == 0 else 3 * a + 1
    if a in s_list:
        break
    s_list.append(a)
    i += 1

ans = i
print(ans)
