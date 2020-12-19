#!/usr/bin/env python3

A, B, C = list(map(int, input().split()))


def is_continue(a, b, c):
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        return True
    return False


a, b, c = A, B, C

if a == b and c == a:
    if is_continue(a, b, c):
        count = -1
    else:
        count = 0
else:
    count = 0
    while is_continue(a, b, c):
        count += 1
        # print(f"[{count}] {tuple(sorted([a, b, c]))}")
        pre_a, pre_b, pre_c = a, b, c
        a = pre_b // 2 + pre_c // 2
        b = pre_c // 2 + pre_a // 2
        c = pre_a // 2 + pre_b // 2

ans = count
print(ans)
