# K = int(input())
K = 10 ** 5
limit_list = []
upper_limit = 9
limit_list.append(upper_limit)
t_dict = {i: 1 for i in range(10)}
# 2桁目の場合
s_dict = {k: 3 for k in range(1, 9)}
s_dict[9] = 2
s_dict[0] = 2
upper_limit = upper_limit + sum(s_dict.values()) - s_dict[0]
limit_list.append(upper_limit)
ww_dict = {1: t_dict, 2: s_dict}  # 2桁目

i = 3
max_limit = 10 ** 5
while upper_limit <= max_limit:
    # 3桁目
    w_dict = {
        k: ww_dict[i - 1][k - 1] + ww_dict[i - 1][k] + ww_dict[i - 1][k]
        for k in range(1, 9)
    }
    w_dict[0] = ww_dict[i - 1][0] + ww_dict[i - 1][1]
    w_dict[9] = ww_dict[i - 1][8] + ww_dict[i - 1][9]
    ww_dict[i] = w_dict
    upper_limit = limit_list[-1] + sum(w_dict.values()) - w_dict[0]
    limit_list.append(upper_limit)
    i += 1

# K = 208644

for i, l in enumerate(limit_list):
    if l >= K:
        keta = i + 1
        break

keta_list = list(range(1, keta + 1))

ans_list = []

# i-1桁目のMAX値
t = limit_list[keta - 2]

for i in keta_list[::-1]:
    # i桁目の数字を決めたい
    if i == keta_list[-1]:
        # iが最大桁の場合の候補の数字
        number_list = list(range(1, 10))
    else:
        if ans_list[-1] == 9:
            max_n = 9
        else:
            max_n = ans_list[-1] + 1
        number_list = list(range(0, max_n + 1))
    for n in number_list:
        if i == 1:
            w = t + 1
        else:
            w = t + ww_dict[i][n]
        print(w)
        if w >= K:
            ans_list.append(n)
            break
        # 超えていなかったら更新
        t = w
    print(ans_list)
    print(t)
    print("-------")

print("------")
print(i)
print(limit_list)
