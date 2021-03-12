#!/usr/bin/env python3
import math

A, B, H, M = list(map(int, input().split()))
h = H - 12 if H >= 12 else H
h_theta = ((h * 60 + M) / (12 * 60)) * 360
m_theta = (M / 60) * 360

theta = max([h_theta, m_theta]) - min([h_theta, m_theta])
theta = 360 - theta if theta >= 180 else theta

c_2 = A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(theta))
ans = math.sqrt(c_2)
print(ans)
