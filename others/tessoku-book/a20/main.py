#!/usr/bin/env python3

S = input()
T = input()

# 縦方向: S
# 横方向: T
# 値: これまでの斜め方向移動の回数
dp_table = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

for i in range(1, len(S) + 1):
    for j in range(len(T) + 1):
        pattern_list = []
        # 縦方向移動から来た場合
        pattern_list.append(dp_table[i - 1][j])
        if j > 0:
            # 横方向移動から来た場合
            pattern_list.append(dp_table[i][j - 1])
            if S[i - 1] == T[j - 1]:
                # 斜め方向移動から来た場合
                pattern_list.append(dp_table[i - 1][j - 1] + 1)
        dp_table[i][j] = max(pattern_list)

ans = dp_table[-1][-1]
print(ans)
