#!/usr/bin/env python3

N = int(input().split()[0])
lr_table = []

for _ in range(N):
    l, r = list(map(int, input().split()))
    lr_table.append((l, r))

# 都度都度判定すると効率が悪いので、
# 1 - 10 ** 5まで全部判定する


def get_prime_number_flag_list(n):
    # エラストネスのふるいを使用
    # 指定されたn以下の数について、素数か素数でないかのリストを返す
    pn_flag_list = [True] * (n + 1)
    pn_flag_list[0] = False
    pn_flag_list[1] = False
    for i in range(2, n + 1):
        if pn_flag_list[i]:
            for j in range(i + i, n + 1, i):
                # 素数ではない
                pn_flag_list[j] = False
    return pn_flag_list


pn_flag_list = get_prime_number_flag_list(10 ** 5)

cumsum_list = []
for i in range(10 ** 5 + 1):
    if i in [0, 1]:
        cumsum_list.append(0)
        continue
    if pn_flag_list[i] and pn_flag_list[(i + 1) // 2]:
        cumsum_list.append(cumsum_list[i - 1] + 1)
    else:
        cumsum_list.append(cumsum_list[i - 1])

count_list = []
for lr_set in lr_table:
    l, r = lr_set
    # l_idx, r_idx = l - 1, r - 1
    count_list.append(cumsum_list[r] - cumsum_list[l - 1])

ans = "\n".join([str(c) for c in count_list])
print(ans)

