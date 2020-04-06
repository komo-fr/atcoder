#!/usr/bin/env python3

X, Y, Z = list(map(int, input().split()))
w = Y
Y = X
X = w

w = Z
Z = X
X = w

ans = "{} {} {}".format(X, Y, Z)
print(ans)
