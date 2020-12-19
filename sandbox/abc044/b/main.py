#!/usr/bin/env python3


from collections import Counter

w = input()
is_ok = True
for k, v in Counter(w).items():
    if v % 2 != 0:
        is_ok = False
        break
ans = "Yes" if is_ok else "No"
print(ans)
