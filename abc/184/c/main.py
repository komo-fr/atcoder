#!/usr/bin/env python3

r1, c1 = list(map(int, input().split()))
r2, c2 = list(map(int, input().split()))

a, b = r1, c1
c, d = r2, c2


def calc_step(a, b):
    if a == c and b == d:
        return True, 0
    if a + b == c + d:
        return True, 1
    elif a - b == c - d:
        return True, 1
    elif abs(a - c) + abs(b - d) <= 3:
        return True, 1
    elif (a + b - c + d) % 2 == 0 or (c + d - a + b) % 2 == 0:
        return True, 2
    return False, -1


if a == c and b == d:
    ans = 0
elif a + b == c + d:
    ans = 1
elif a - b == c - d:
    ans = 1
elif abs(a - c) + abs(b - d) <= 3:
    ans = 1
elif (a + b - c + d) % 2 == 0 or (c + d - a + b) % 2 == 0:
    ans = 2
else:
    min_count = float("inf")
    for x in range(-2, 3):
        for y in range(-2, 3):
            count = 1
            a_ = a + x
            b_ = b + y
            r, step = calc_step(a_, b_)
            if r:
                count += step
            else:
                count = 3
            min_count = min([min_count, count])
    for x, y in [(-3, 0), (3, 0), (0, -3), (0, 3)]:
        count = 1
        a_ = a + x
        b_ = b + y
        r, step = calc_step(a_, b_)
        if r:
            count += step
        else:
            count = 3
        min_count = min([min_count, count])

    ans = min_count

print(ans)
