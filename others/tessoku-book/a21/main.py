#!/usr/bin/env python3

N = int(input().split()[0])
pa_list = []

for _ in range(N):
    p, a = list(map(int, input().split()))
    pa_list.append((p, a))

# 縦方向: 残っている左端のインデックス（Nまで）
# 横方向: 残っている右端のインデックス（Nまで）
# 値: 得点
dp_table = [[0] * N for _ in range(N)]

for diff in range(N - 1, -1, -1):
    for l in range(N - diff):
        r = l + diff
        d_list = [0]
        if l > 0:
            # 直前で左ブロックをとったルート
            # l-1を対象のブロックより先にとったら得点
            p_index = pa_list[l - 1][0] - 1  # 格納されてる数字は1大きいので引く
            a = pa_list[l - 1][1] if l <= p_index <= r else 0
            d_list.append(dp_table[l - 1][r] + a)

        if r < N - 1:
            # 直前で右ブロックをとったルート
            # r+1を対象のブロックより先にとったら得点
            p_index = pa_list[r + 1][0] - 1
            a = pa_list[r + 1][1] if l <= p_index <= r else 0
            d_list.append(dp_table[l][r + 1] + a)

        dp_table[l][r] = max(d_list)

last_list = []
for i in range(N):
    last_list.append(dp_table[i][i])

ans = max(last_list)
print(ans)
