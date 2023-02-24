#!/usr/bin/env python3

N, S = list(map(int, input().split()))
a_list = list(map(int, input().split()))

# 縦方向: 何番目の数字まで考えるか（N+1個用意）
# 横方向: 合計値（S+1個用意）
# 値: i番目の数字まで考えた時に合計値をjにすることが可能かどうか（True/False）
dp_table = [[False] * (S + 1) for _ in range(N + 1)]
dp_table[0][0] = True

for i in range(1, N + 1):
    a_index = i - 1
    for j in range(S + 1):
        if dp_table[i - 1][j]:
            # i番目の数字を選ばない場合
            dp_table[i][j] = True
            # i番目の数字を選ぶ場合
            if j + a_list[a_index] < S + 1:
                dp_table[i][j + a_list[a_index]] = True

ans = "Yes" if dp_table[-1][-1] else "No"
print(ans)
