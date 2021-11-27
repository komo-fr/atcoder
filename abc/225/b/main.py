#!/usr/bin/env python3
from collections import defaultdict

N = int(input().split()[0])

a_0, b_0 = list(map(int, input().split()))
a_1, b_1 = list(map(int, input().split()))
center = None
if a_0 == a_1 or a_0 == b_1:
    center = a_0
elif b_0 == a_1 or b_0 == b_1:
    center = b_0

if center is not None:
    ans = "Yes"
    for _ in range(N - 3):
        a, b = list(map(int, input().split()))
        if center not in [a, b]:
            ans = "No"
else:
    ans = "No"

print(ans)
