#!/usr/bin/env python3

N, K, A = list(map(int, input().split()))

if N == 1:
    ans = 1
else:
    K = K % N
    if (A + K - 1) <= N:
        ans = A + K - 1
    else:
        ans = K - (N - A + 1)

print(ans)
