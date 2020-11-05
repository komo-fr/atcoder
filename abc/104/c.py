# https://atcoder.jp/contests/abc104/tasks/abc104_c
# C - All Green
import itertools

D, G = list(map(int, input().split()))
pc_list = []
for _ in range(D):
    p, c = list(map(int, input().split()))
    pc_list.append((p, c))

# 完全にとく or 途中までとく or 全くとかない パターンがある
# 各問題ごとに、完全にとくかどうかの組み合わせ
p_gen = itertools.product([0, 1], repeat=D)

cost_list = []
for pattern in p_gen:
    cost = 0
    point = 0
    for i, solve_flag in enumerate(pattern):
        point += ((i+1) * 100 * pc_list[i][0] + pc_list[i][1]) * solve_flag
        cost += pc_list[i][0] * solve_flag

    if point >= G:
        # 解けた場合
        cost_list.append(cost)
    else:
        # 解けない場合は、完全にといていない問題のうち次に配点が高いもので埋める
        # ただし、完全にとくことはできないので、各問題で使えるのはp-1問まで
        kouho_list = [i for i, solve_flag in enumerate(pattern) if solve_flag == 0]
        kouho_list = sorted(kouho_list, reverse=True)
        is_over = False
        for i in kouho_list:
            for _ in range(1, pc_list[i][0]):
                point += (i+1) * 100
                cost += 1
                if point >= G:
                    is_over = True
                    break
            if is_over:
                break
        if is_over:
            cost_list.append(cost)

ans = min(cost_list)
print(ans)
