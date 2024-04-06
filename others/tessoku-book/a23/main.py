#!/usr/bin/env python3

N, M = list(map(int, input().split()))
a_list = []

for _ in range(M):
    _a_list = list(map(int, input().split()))
    a = int("".join([str(i) for i in reversed(_a_list)]), 2)
    a_list.append(a)

# 縦方向: 何個までのクーポンについて考えるか（M+1個用意）
# 横方向: 無料で得られる商品を表した集合（2進数で考える。たとえば商品1,3が得られる場合は101で5）（2**N個用意）
# 値: 使用したクーポンの数。最小値を入れる
dp_table = [[float("inf")] * (2 ** N) for _ in range(M + 1)]
dp_table[0][0] = 0

for i in range(1, M + 1):
    # i番目のクーポンについて考える
    for j in range(2 ** N):
        # 現在、集合jの商品が無料で得られる

        if dp_table[i - 1][j] <= M:
            # i番目のクーポンを使った場合に無料で得られる商品の集合
            a_index = i - 1
            target_index = a_list[a_index] | j
            # i番目のクーポンを使う場合
            if target_index < 2 ** N:
                dp_table[i][target_index] = min(
                    [dp_table[i - 1][j] + 1, dp_table[i][target_index]]
                )

            # i番目のクーポンを使わない場合
            dp_table[i][j] = min([dp_table[i - 1][j], dp_table[i][j]])

ans = dp_table[-1][-1] if dp_table[-1][-1] < N else -1
print(ans)
