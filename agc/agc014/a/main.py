#!/usr/bin/env python3

A, B, C = list(map(int, input().split()))


def is_continue(x_list):
    for x in x_list:
        if x % 2 == 1:
            return False
    return True


count = 0

while is_continue([A, B, C]):
    if A == B and B == C:
        count = -1
        break
    a, b, c = A, B, C
    a = B // 2 + C // 2
    b = A // 2 + C // 2
    c = A // 2 + B // 2
    A, B, C = a, b, c
    count += 1

ans = count
print(ans)
