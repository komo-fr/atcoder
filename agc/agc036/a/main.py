#!/usr/bin/env python3

S = int(input().split()[0])
x_1, y_1 = 0, 0
x_2, y_2 = 1, 0
x_3, y_3 = 1, S


def get_divisor(n: int) -> list:
    d_list = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            a = int(n / i)
            if a <= 10 ** 9 and i <= 10 ** 9:
                d_list.append((i, a))
                break
    return d_list


d_list = get_divisor(S)
x_2 = d_list[0][0]
x_3 = x_2
y_3 = d_list[0][1]
ans = " ".join([str(x) for x in [x_1, y_1, x_2, y_2, x_3, y_3]])

print(ans)
