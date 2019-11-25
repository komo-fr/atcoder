#!/usr/bin/env python3

A, B, X = list(map(int, input().split()))
for d in range(10):
    if A * 10 ** d + B * (d + 1) > X:
        break

d = d - 1
N = (X - B * (d + 1)) // A
# N = N - 1 if len(str(N)) != (d + 1) else N


def calc(n):
    return A * n + B * len(str(n))


while True:
    if calc(N) <= X < calc(N + 1):
        break
    elif calc(N) > X:
        N -= 1
    elif X >= calc(N + 1):
        N += 1

ans = min(N, 10 ** 9)
ans = 0 if ans < 0 else ans
print(ans)
