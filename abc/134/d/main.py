#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))

# 最初が0から始まる場合
b_list = [0] * N
b_list[-1] = a_list[-1]

for i in range(1, N + 1):
    # 大きい方から決めていく
    idx = N - i
    total = 0
    for j in b_list[:: idx + 1]:
        # idx + 1の倍数のボールの個数を数える
        total += b_list[j]

    if total % (idx + 1) != a_list[idx]:
        b_list[idx] = 1

idx_list = [str(i + 1) for i, b in enumerate(b_list) if b == 1]
ans = sum(b_list)
print(ans)
print(" ".join(idx_list))
