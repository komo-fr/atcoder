#!/usr/bin/env python3
import math

x1, y1, r = list(map(int, input().split()))
x2, y2, x3, y3 = list(map(int, input().split()))

circle_point = [(x1, y1 + r), (x1, y1 - r), (x1 + r, y1), (x1 - r, y1)]

# 円が四角形の中におさまっていないどうか(赤が残っているかどうか)
is_red = True
if (y2 <= y1 + r <= y3) and (y2 <= y1 - r <= y3):
    if (x2 <= x1 + r <= x3) and (x2 <= x1 - r <= x3):
        is_red = False

# 四角形が円におさまっていないかどうか（青が残っているかどうか）


def is_inside_circle(x, y):
    if x1 - r <= x <= x1 + r:
        if y >= y1:
            if y <= (y1 + math.sqrt(r ** 2 - (x - x1) ** 2)):
                return True
        else:
            if y >= (y1 - math.sqrt(r ** 2 - (x - x1) ** 2)):
                return True
    return False


is_blue = False
rect_point_list = [(x2, y2), (x3, y2), (x2, y3), (x3, y3)]

for p in rect_point_list:
    p_x, p_y = p
    if not is_inside_circle(p_x, p_y):
        is_blue = True
        break

ans_red = "YES" if is_red else "NO"
print(ans_red)

ans_blue = "YES" if is_blue else "NO"
print(ans_blue)
