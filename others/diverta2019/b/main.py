#!/usr/bin/env python3

R, G, B, N = list(map(int, input().split()))

max_r = N // R
max_g = N // G
max_b = N // B

count = 0
for r in range(max_r + 1):
    for g in range(max_g + 1):
        now_n = r * R + g * G
        if now_n <= N and (N - now_n) % B == 0:
            b = (N - now_n) // B
            count += 1

ans = count

print(ans)
