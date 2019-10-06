# https://atcoder.jp/contests/abc032/tasks/abc032_d
# D - ナップサック問題
import copy

n, w = list(map(int, input().split()))
vw_list = []

for _ in range(n):
    work_v, work_w = list(map(int, input().split()))
    vw_list.append((work_v, work_w))

dp_table = [[0] * (w + 1)]

# この方法だと計算効率的にNG
# 価値について逆順にして考えた方がよいはず
for i in range(n):
    dp_list = dp_table[i]
    value, weight = vw_list[i]
    next_dp_list = copy.copy(dp_list)

    for w_i, now_value in enumerate(dp_list):
        if w_i != 0 and now_value == 0:
            continue

        # 重量オーバーにならないか？
        if w_i + weight > w:
            # 重量オーバー
            continue

        # 荷物を追加した場合、価値の最大を更新するか？
        if dp_list[w_i] + value > dp_list[w_i + weight]:
            next_dp_list[w_i + weight] = dp_list[w_i] + value

    dp_table.append(next_dp_list)

print(dp_table)
ans = max(dp_table[-1])
print(ans)
