#!/usr/bin/env python3
from decimal import Decimal, ROUND_HALF_UP


deg, dis = list(map(int, input().split()))
kakudo_list = [(11.25 + 22.5 * i, 11.25 + 22.5 * (i + 1)) for i in range(15)]
kakudo_name_list = [
    "NNE",
    "NE",
    "ENE",
    "E",
    "ESE",
    "SE",
    "SSE",
    "S",
    "SSW",
    "SW",
    "WSW",
    "W",
    "WNW",
    "NW",
    "NNW",
]

kakudo_name = "N"
# fusoku_list = [(2 * i, 2 * (i + 1)) for i in range(12)]
fusoku_list = [
    (0, 0.2),
    (0.3, 1.5),
    (1.6, 3.3),
    (3.4, 5.4),
    (5.5, 7.9),
    (8.0, 10.7),
    (10.8, 13.8),
    (13.9, 17.1),
    (17.2, 20.7),
    (20.8, 24.4),
    (24.5, 28.4),
    (28.5, 32.6),
]
# 角度
for i, kakudo in enumerate(kakudo_list):
    if kakudo[0] <= deg / 10 <= kakudo[1]:
        kakudo_name = kakudo_name_list[i]

fusoku = dis / 60
y = float(Decimal(str(fusoku)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
# print(fusoku_list)
# print(f"y={y}")
furyoku = 12
for i, f in enumerate(fusoku_list):
    if f[0] <= y <= f[1]:
        furyoku = i
        break
kakudo_name = "C" if furyoku == 0 else kakudo_name
ans = f"{kakudo_name} {furyoku}"
print(ans)
