#!/usr/bin/env python3

A, B, C = list(map(int, input().split()))
exist_even = False

for x in [A, B, C]:
    if x % 2 == 0:
        exist_even = True
        ans = 0
        break

if not exist_even:
    ans_1 = (A + 1) // 2 * B * C - (A - 1) // 2 * B * C
    ans_2 = (B + 1) // 2 * A * C - (B - 1) // 2 * A * C
    ans_3 = (C + 1) // 2 * B * A - (C - 1) // 2 * B * A
    ans = min([ans_1, ans_2, ans_3])

print(ans)
