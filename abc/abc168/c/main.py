#!/usr/bin/env python3
import math

A, B, H, M = list(map(int, input().split()))

# 分針
m_d = 360 * (M / 60)
# 時針
h_d = 360 * (((60 * H) + M) / (60 * 12))

x = abs(m_d - h_d)
y = 360 - x
C_d = min(x, y)

C = A ** 2 + B ** 2 - (2 * A * B * math.cos(math.radians(C_d)))
ans = math.sqrt(C)
print(ans)
