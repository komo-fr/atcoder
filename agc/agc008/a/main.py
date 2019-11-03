#!/usr/bin/env python3

x, y = list(map(int, input().split()))

if x == y:
    count = 0
elif x == 0:
    count = abs(y)
    if y < 0:
        count += 1
elif y == 0:
    count = abs(x)
    if x > 0:
        count += 1
else:
    if x * y < 0:
        # x と yの符号が違う
        # -10, 5
        # -5, 10
        # 10, -5
        # 5, -10
        if abs(x) == abs(y):
            count = 1
        elif x < y:
            # xが負、yが正
            count = abs(x - y)
            count_2 = 1 + abs(abs(x) - abs(y))
            count = min(count, count_2)
        else:
            count = 1 + abs(abs(x) - abs(y))

    else:
        # xとyの符号が同じ
        if x < y:
            count = abs(y - x)
        else:
            count = 2
            count += abs(y - x)

ans = count
print(ans)
