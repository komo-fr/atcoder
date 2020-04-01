#!/usr/bin/env python3

X = int(input().split()[0])
t = 0
t += (X // 500) * 1000
t += ((X % 500) // 5) * 5
print(t)
