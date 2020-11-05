#!/usr/bin/env python3
from decimal import Decimal, ROUND_HALF_UP

deg, dis = list(map(int, input().split()))
deg /= 10

dis /= 60
dis = float(Decimal(str(dis)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))

deg_list = [
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

deg_dict = {
    v: [11.25 + 22.5 * i, 11.25 + 22.5 * (i + 1)] for i, v in enumerate(deg_list)
}

d = "N"
for k, v in deg_dict.items():
    if v[0] <= deg < v[1]:
        d = k
        break

w_list = [
    [0.0, 0.2],
    [0.3, 1.5],
    [1.6, 3.3],
    [3.4, 5.4],
    [5.5, 7.9],
    [8.0, 10.7],
    [10.8, 13.8],
    [13.9, 17.1],
    [17.2, 20.7],
    [20.8, 24.4],
    [24.5, 28.4],
    [28.5, 32.6],
]
w_dict = {i: v for i, v in enumerate(w_list)}
w = 12

for k, v in w_dict.items():
    if v[0] <= dis <= v[1]:
        w = k
        break

if w == 0:
    d = "C"

ans = "{} {}".format(d, w)
print(ans)
