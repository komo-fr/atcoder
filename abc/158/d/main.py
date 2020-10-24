#!/usr/bin/env python3

S = input()
Q = int(input().split()[0])
s = S
flag = True

for _ in range(Q):
    q = list(input().split())
    if len(q) == 1:
        flag = not flag
    else:
        _, f, c = q
        if flag:
            s = c + s if f == "1" else s + c
        else:
            s = s + c if f == "1" else c + s
if not flag:
    s = s[::-1]

ans = s
print(ans)
