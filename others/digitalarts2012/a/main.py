#!/usr/bin/env python3

s_list = input().split()
N = int(input().split()[0])
ng_list = []

for _ in range(N):
    t = input()
    ng_list.append(t)
after_list = []
for s in s_list:
    for t in ng_list:
        is_ok = False
        if len(s) != len(t):
            is_ok = True
            continue
        for i, char_t in enumerate(t):
            if char_t != "*" and char_t != s[i]:
                is_ok = True
                break
        if not is_ok:
            break
    a = s if is_ok else "*" * len(s)
    after_list.append(a)

ans = " ".join(after_list)
print(ans)
