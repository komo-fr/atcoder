#!/usr/bin/env python3
N, W = list(map(int, input().split()))
wv_list = []

for _ in range(N):
    w, v = list(map(int, input().split()))
    wv_list.append((w, v))

# 縦方向: 何個までの商品について考えるか（N+1まで）
# 横方向: 重さの合計（W+1まで）
# 値: 価値の合計
dp_table = [[-float("inf")] * (W + 1) for _ in range(N + 1)]
dp_table[0][0] = 0

for i in range(1, N + 1):
    wv_index = i - 1
    for j in range(W + 1):
        if dp_table[i - 1][j] >= 0:
            # 商品iを選ばなかった場合
            dp_table[i][j] = max([dp_table[i - 1][j], dp_table[i][j]])
            # 商品を選んだ場合
            w, v = wv_list[wv_index]
            if j + w <= W:
                # 重さの上限を超えない
                dp_table[i][j + w] = max([dp_table[i - 1][j] + v, dp_table[i][j + w]])

ans = max(dp_table[-1])
print(ans)
