#!/usr/bin/env python3

K = int(input())

# Xがi+1桁である場合のルンルン数の最大値のリスト
limit_list = []

# Xが1桁の場合のルンルン数の最大値
upper_limit = 9
limit_list.append(upper_limit)

# 1桁目がiである場合のルンルン数の個数
w_dict = {i: 1 for i in range(10)}

max_K = 10 ** 5
i = 2

# i桁目の数字がkである場合のルンルン数の個数をあらかじめカウントしておく
# ww_dictのキーは桁数
ww_dict = {1: w_dict}

while upper_limit <= max_K:
    w_dict = {
        k: ww_dict[i - 1][k - 1] + ww_dict[i - 1][k] + ww_dict[i - 1][k + 1]
        for k in range(1, 9)
    }
    w_dict[0] = ww_dict[i - 1][0] + ww_dict[i - 1][1]
    w_dict[9] = ww_dict[i - 1][8] + ww_dict[i - 1][9]
    ww_dict[i] = w_dict
    upper_limit = limit_list[-1] + sum(w_dict.values()) - w_dict[0]
    limit_list.append(upper_limit)
    i += 1

# 各桁におけるルンルン数の最大値から、Kの桁数を求める
for i, l in enumerate(limit_list):
    if l >= K:
        digit_n = i + 1
        break

# Xの各桁における数字のリスト
x_list = []

# 「Kの最大桁-1」の桁数におけるルンルン数の最大値
lunlun_k = limit_list[(digit_n - 1) - 1]

if digit_n == 1:
    # 1桁の場合は確定でX=Kになる
    x_list = [K]
else:
    # i桁目の数字を、大きい桁から決めていく
    for i, digit in enumerate(reversed(range(1, digit_n + 1))):
        if i == 0:
            # iが最大桁である場合の数字の候補（leading zero無なので0は含まない）
            number_list = list(range(1, 10))
        else:
            # iが最大桁ではない場合、直前に決めた桁によって候補が変わる
            max_n = 9 if x_list[-1] == 9 else x_list[-1] + 1
            min_n = 0 if x_list[-1] == 0 else x_list[-1] - 1
            number_list = list(range(min_n, max_n + 1))

        for n in number_list:
            tmp_lunlun_k = lunlun_k + ww_dict[digit][n]

            if tmp_lunlun_k >= K:
                # i桁目の数字はnで確定
                x_list.append(n)
                break

            # i桁目は少なくともn以上の数なので続行
            lunlun_k = tmp_lunlun_k

ans = "".join([str(i) for i in x_list])
print(ans)
