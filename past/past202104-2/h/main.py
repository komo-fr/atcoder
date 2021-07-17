#!/usr/bin/env python3
import heapq
from collections import deque
import math

N, M, K, Q = list(map(int, input().split()))
a_can_list = []
b_can_list = []

for _ in range(N):
    p, t = list(map(int, input().split()))
    if t == 1:
        # 缶切りがいる
        b_can_list.append(p)
    else:
        a_can_list.append(p)

b_can_n = len(b_can_list)
a_can_n = N - b_can_n
a_can_list = sorted(a_can_list)
b_can_list = sorted(b_can_list)


# 最大で必要な缶切りの数
max_k = math.ceil(b_can_n / K)
# min_k = 0
if a_can_n < M:
    # 缶切りが必要な缶の最低数
    min_k = math.ceil((M - a_kankiri_can_n) / K)

elif a_can_n > M:
    # 先頭M個まで見れば良い
    a_can_list = a_can_list[:M]

if b_can_n > M:
    # 先頭M個まで見れば良い
    b_can_list = b_can_list[:M]

a_can_q = deque(a_can_list)
b_can_q = deque(b_can_list)

kankiri_cost = 0
min_cost = float("inf")

a_can_cost = sum(list(a_can_q))
each_step_min_cost_list = [0]

# print(a_can_list)
# print(b_can_list)

for kankiri_N in range(max_k+1):
    # kankiri_N = 手持ちの缶切りの数
    # print("==============")
    # print(f"前ステップでの最小: {each_step_min_cost_list[-1]}")

    if kankiri_N == 0:
        if a_can_n < M:
            # 缶切り使うしかない
            continue
        this_step_min_cost = a_can_cost
        each_step_min_cost_list.append(this_step_min_cost)
        continue
    # 缶切りを使う
    this_step_min_cost = each_step_min_cost_list[-1] + Q
    # print(f"缶のコスト+{Q}")
    tmp_cost = this_step_min_cost
    
    for k in range(K):
        # k = 追加で開ける缶の数
        if a_can_q and b_can_q:
            removed_a_can_cost = a_can_q.pop()
            additional_b_can_cost = b_can_q.popleft()
            # 入れ変えた場合のコスト
            diff_cost = removed_a_can_cost - additional_b_can_cost
            tmp_cost -= diff_cost
            # print(f"A缶（{removed_a_can_cost}）->B缶({additional_b_can_cost}) よって{diff_cost}削減して{tmp_cost}")    
            this_step_min_cost = min([this_step_min_cost, tmp_cost])
    each_step_min_cost_list.append(this_step_min_cost)    

# print(each_step_min_cost_list)
ans = min(each_step_min_cost_list[1:])
print(ans)
