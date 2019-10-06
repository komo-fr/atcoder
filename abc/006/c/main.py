#!/usr/bin/env python3

N, M = list(map(int, input().split()))

is_ok = False
for i in range(0, 2):
    nokori_n = N - i  # 2または4の個数 N = 人間の数
    nokori_m = M - 3 * i  # 2または4で埋める足の数 M = 足の数

    if nokori_m % 2 == 0:
        # まかなえる
        for j in range(N - i + 1):  # 大人と赤ちゃんの数
            k = N - i - j
            if i * 3 + j * 2 + k * 4 == M:
                is_ok = True
                ans = (j, i, k)
                break

if not is_ok:
    ans = (-1, -1, -1)

ans = "{} {} {}".format(ans[0], ans[1], ans[2])

print(ans)
