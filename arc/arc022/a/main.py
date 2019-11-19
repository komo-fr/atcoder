#!/usr/bin/env python3

S = input()
sub_s = ""

for char in S:
    char = char.lower()
    if char == "i" and sub_s == "":
        sub_s = "i"
    elif char == "c" and sub_s == "i":
        sub_s = "ic"
    elif char == "t" and sub_s == "ic":
        sub_s = "ict"

ans = "YES" if sub_s == "ict" else "NO"

print(ans)
