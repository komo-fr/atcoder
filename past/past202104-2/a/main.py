#!/usr/bin/env python3

S = input()
targets = "0123456789"
is_ok = True
for i, s in enumerate(S):
    if i == 3:
        if s != "-":
            is_ok = False
            break
    else:
        if s not in targets:
            is_ok = False
            break
ans = "Yes" if is_ok  else "No"
print(ans)
