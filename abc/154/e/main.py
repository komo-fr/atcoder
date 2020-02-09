#!/usr/bin/env python3
import itertools


N = int(input().split()[0])
K = int(input().split()[0])
# base = '0' * len(str(N))
n_str = str(N)
len_n = len(n_str)
l = list(range(len_n))
p_list = list(itertools.combinations(l, K))

total = 0
if K == 1:
    for pattern in p_list:
        y = pattern[0]  # y桁目
        # 最大桁の場合
        if y == 0:
            total += int(n_str[0])
        else:
            # 最大桁ではない場合
            total += 9
elif K == 2:
    # 1つが最大桁の場合は
    for pattern in p_list:
        pattern = sorted(list(pattern))
        y = pattern[0]  # y桁目
        # 最大桁の場合
        if y == 0:
            w = int(n_str[0])
            total += (w - 1) * 9 + 1 * int(n_str[1])
        else:
            # 最大桁ではない場合
            total += 9 ** 2
elif K == 3:
    # 1つが最大桁の場合は
    for pattern in p_list:
        pattern = sorted(list(pattern))

        w1 = int(n_str[0])
        w2 = int(n_str[1])
        w3 = int(n_str[2])

        if 0 in pattern:
            # 最大桁が0確定: 何を選んでも良い
            total += 9 ** 3
        else:
            # 最大桁が0ではない
            if 1 in pattern:
                # if 1 in pattern and w2 != 0:
                # 2番目の桁が0確定: 2個目以降は何を選んでも良い
                w1 = int(n_str[0])
                total += w1 * 9 * 9
            else:
                # 最大桁も2番目の桁も0ではない
                total += (w1 - 1) * 9 * 9
                total += 1 * (w2 - 1) * 9
                total += 1 * 1 * w3

ans = total
print(ans)
