#!/usr/bin/env python3
import math

A, K = list(map(int, input().split()))

goal = 2 * 10 ** 12

if K == 0:
    d = goal - A
elif A == 0:
    d = math.ceil(math.log(goal, K + 1)) + 1
else:
    d = math.ceil(math.log(goal / A, K + 1))

print(d)
