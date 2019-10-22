#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))

# 最初が0から始まる場合
a_list = [0] + a_list
b_list = [0] * (N + 1)
# インデックスがずれるのがややこしいので、
# b_list[0]は欠番として1始まりで考えていく

for i in range(N):
    # 大きい方から決めていく
    idx = N - i
    total = sum(b_list[idx : N + 1 : idx])

    if total % 2 != a_list[idx]:
        b_list[idx] = 1

idx_list = [str(i) for i, b in enumerate(b_list) if b == 1]
ans = sum(b_list[1:])
print(ans)
if ans != 0:
    print(" ".join(idx_list))
