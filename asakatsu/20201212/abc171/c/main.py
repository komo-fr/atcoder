#!/usr/bin/env python3
import string

N = int(input().split()[0])
str2n = string.ascii_lowercase

n = N
text = ""
while n > 0:
    n -= 1
    amari = n % 26
    text += str2n[amari]
    n = n // 26
ans = text[::-1]

print(ans)
