#!/usr/bin/env python3
import collections

S = input()
Q = int(input().split()[0])
s = collections.deque(list(S))
flag = True

for _ in range(Q):
    q = list(input().split())
    if len(q) == 1:
        flag = not flag
    else:
        _, f, c = q
        if flag:
            if f == "1":
                s.appendleft(c)
            else:
                s.append(c)
        else:
            if f == "1":
                s.append(c)
            else:
                s.appendleft(c)

if not flag:
    s = "".join(list(s)[::-1])
else:
    s = "".join(s)

ans = s
print(ans)
