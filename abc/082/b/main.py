#!/usr/bin/env python3

s = input()
t = input()

s = "".join(list(sorted(s)))
t = "".join(list(sorted(t, reverse=True)))
ans = "Yes" if s < t else "No"
print(ans)
