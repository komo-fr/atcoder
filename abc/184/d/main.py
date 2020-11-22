#!/usr/bin/env python3

A, B, C = list(map(int, input().split()))

a = 100 - A
b = 100 - B
c = 100 - C
first_total = a + b + c

# Aで終わる場合Aはa回操作する, Bは0〜b-1, Cは0〜c-1回操作する
ans = a * (a / first_total) + (b - 1) * (b / first_total) + (c - 1)(c / first_total)


print(ans)
