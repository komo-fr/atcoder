#!/usr/bin/env python3

S = input()
r_a_count = len(S) - len(S.rstrip("a"))
l_a_count = len(S) - len(S.lstrip("a"))

s = S.strip("a")
is_ok = False
if list(reversed(s)) == list(s) and r_a_count >= l_a_count:
    is_ok = True

ans = "Yes" if is_ok else "No"
print(ans)
