#!/usr/bin/env python3

L, X, Y, S, D = list(map(int, input().split()))

clockwise_s = X + Y
anti_clockwise_s = Y - X

if S == D:
    ans = 0
else:
    if S > D:
        anti_clockwise_l = S - D
        clockwise_l = L - anti_clockwise_l
    else:
        clockwise_l = D - S
        anti_clockwise_l = abs(clockwise_l - L)

    if anti_clockwise_s > 0:
        ans = min(clockwise_l / clockwise_s, anti_clockwise_l / anti_clockwise_s)
    else:
        ans = clockwise_l / clockwise_s

print(ans)
