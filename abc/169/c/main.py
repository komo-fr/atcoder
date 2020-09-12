#!/usr/bin/env python3

A, B = list(input().split())
a = int(A)
b = int(B.replace(".", ""))

ans = (a * b) // 100

print(ans)
