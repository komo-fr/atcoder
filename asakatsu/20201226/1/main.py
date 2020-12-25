#!/usr/bin/env python3
from collections import Counter

S, T = list(map(str, input().split()))
A, B = list(map(int, input().split()))
U = input()
if S == U:
    A -= 1
else:
    B -= 1

print(A, B)
