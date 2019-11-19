#!/usr/bin/env python3

N = int(input().split()[0])

keta = N // 9
hasu = N % 9
hasu = 9 if hasu == 0 else hasu
keta = keta - 1 if hasu == 9 else keta

ans = str(hasu) * (keta + 1)

print(ans)
