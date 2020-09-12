#!/usr/bin/env python3
from cmath import e
import string

N = int(input().split()[0])
a_list = string.ascii_lowercase

amari_list = []
n = N
while n != 0:
    quo = n // 26
    amari = n % 26
    amari_list.append(amari - 1)
    n = quo

ans = "".join([a_list[amari] for amari in reversed(amari_list)])

print(ans)
