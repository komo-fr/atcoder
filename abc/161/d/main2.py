#!/usr/bin/env python3

K = int(input())
n_list = list(range(1, 10))

for i in range(1, K + 1):
    # 桁数
    digit = i // 10 + 1
    n = i % 10
    if digit == 1:
        # Kが1桁の場合は、X=Kになる
        x = i
        continue
    # 今の数はx
