#!/usr/bin/env python3
import string

S = input()
ki = ""
for char in S:
    if char in string.ascii_lowercase + string.ascii_uppercase:
        continue
    ki += char

ans = ki
print(ans)
