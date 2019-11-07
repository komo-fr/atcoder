#!/usr/bin/env python3

N = int(input().split()[0])
s = input()
t = input()

for i in range(N):
    if s[i] == t[0]:
        is_ok = True
        for j in range(N - i):
            if s[j + i] != t[j]:
                is_ok = False
                break
        if is_ok:
            start_idx = i
            break
    else:
        is_ok = False

if is_ok:
    l = N + start_idx
else:
    l = N * 2

ans = l
print(ans)
