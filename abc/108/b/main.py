#!/usr/bin/env python3

x_1, y_1, x_2, y_2 = list(map(int, input().split()))
if x_1 == x_2:
    if y_2 > y_1:
        x_3, y_3 = x_1 - abs(y_1 - y_2), y_2
        x_4, y_4 = x_3, y_1
    else:
        x_3, y_3 = x_1 + abs(y_1 - y_2), y_2
        x_4, y_4 = x_3, y_1
else:
    if x_1 > x_2:

x_3, y_3 = x_2, y_1 + abs(x_2 - x_1)
x_4, y_4 = x_1, y_3

ans = "{} {} {} {}".format(x_3, y_3, x_4, y_4)
print(ans)
