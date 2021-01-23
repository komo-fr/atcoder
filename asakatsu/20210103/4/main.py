#!/usr/bin/env python3
from collections import Counter

S = input()
T = int(input().split()[0])

c = Counter(S)

# y軸方向の差分
y_d = abs(c["U"] - c["D"])
x_d = abs(c["R"] - c["L"])

if T == 1:
    # 最大値
    ans = y_d + x_d + c["?"]
else:
    d = x_d + y_d
    if c["?"] <= d:
        ans = d - c["?"]
    else:
        ans = 0 if (c["?"] - d) % 2 == 0 else 1

print(ans)
