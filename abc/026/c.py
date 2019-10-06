# https://atcoder.jp/contests/abc026/tasks/abc026_c
# C - 高橋君の給料

n = int(input().split()[0])
b_list = []
for _ in range(n - 1):
    b = int(input().split()[0])
    b_list.append(b)

# 末端社員
leaf_list = list(set(range(1, n+1)) - set(b_list))
b_dict = {k: dict(p=None, boss=None, sub_list=[], sub_p_list=[]) for k in range(1, n+1)}

for i, boss in enumerate(b_list):
    personal_no = i+2
    # 上司の社員番号を登録
    b_dict[personal_no]['boss'] = boss
    # 部下の社員番号を登録
    b_dict[boss]['sub_list'].append(personal_no)

# 給与計算が終わった社員の社員番号
done_list = []

# 末端社員から給与計算
next_kouho_list = []
# print('leaf: {}'.format(leaf_list))
for no in leaf_list:
    # 自分の給与を計算
    b_dict[no]['p'] = 1

    # ボスに自分の給与を教える
    boss = b_dict[no]['boss']
    b_dict[boss]['sub_p_list'].append(1)
    done_list.append(no)
    # 次の探索対象の候補
    next_kouho_list.append(b_dict[no]['boss'])

next_kouho_list = list(set(next_kouho_list))
# print(next_kouho_list)
c = 0

while len(done_list) < n:
    # c += 1
    # print(c)
    work_kouho_list = []
    for kouho_no in next_kouho_list:
        # 部下全員の給与計算が終わっているか
        # print('sub_list: {}'.format(set(b_dict[kouho_no]['sub_list'])))
        # print('done_list: {}'.format(done_list))

        if set(done_list).issuperset(set(b_dict[kouho_no]['sub_list'])):
            # 給与計算
            sub_p_list = b_dict[kouho_no]['sub_p_list']
            p = max(sub_p_list) + min(sub_p_list) + 1

            # 自分の給与
            b_dict[kouho_no]['p'] = p
            boss = b_dict[kouho_no]['boss']

            if boss:
                # ボスに自分の給与を教える
                b_dict[boss]['sub_p_list'].append(p)
                # 当該社員のボスを次の候補に追加
                work_kouho_list.append(boss)
            done_list.append(kouho_no)

        else:
            # 部下の給与計算が終わっていない
            work_kouho_list.append(kouho_no)

    next_kouho_list = list(set(work_kouho_list))

print(b_dict[1]['p'])
