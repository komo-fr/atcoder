#!/usr/bin/env python3

S = input()
is_ok = True
for i, ch in enumerate(list(S)):
    if i % 2 == 0:
        if ch not in "RUD":
            is_ok = False
    else:
        if ch not in "LUD":
            is_ok = False

ans = "Yes" if is_ok else "No"

print(ans)
