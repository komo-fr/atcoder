#!/usr/bin/env python3
from cmath import e
import string

N = int(input().split()[0])
a_list = string.ascii_lowercase
w = 26
i = 1

while N > w:
    i += 1
    w += 26 ** i
    print(i)
    print(w)

keta = i
w = N
amari_list = []
print(f"keta={keta}")
while keta > 0:
    print(w)

    amari = w % (26 ** (keta - 1))
    amari_list.append(amari)
    w = w // (26 ** (keta - 1))
    keta -= 1

text = ""
print(amari_list)
for i, amari in enumerate(amari_list):
    if i == len(amari_list) - 1:
        text += a_list[amari - 1]
    else:
        text += a_list[amari]

ans = text
print(ans)
