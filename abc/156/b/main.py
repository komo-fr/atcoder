#!/usr/bin/env python3

N, K = list(map(int, input().split()))


def conv(X, n):
    if int(X / n):
        return conv(int(X / n), n) + str(X % n)
    return str(X % n)


ans = len(str(conv(N, K)))

print(ans)
