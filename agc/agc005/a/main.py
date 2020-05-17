#!/usr/bin/env python3

X = input()
N = len(X)
after_x = ""
next_i = 0
# 連続する箇所で部分文字列を作りたい
s_count, t_count = 0, 0
if X[0] == "T":
    # Tから始まる場合、最初の連続するTは確定で残るので切り捨てる
    for i, x in enumerate(X):
        if x == "T":
            after_x += x
        else:
            break
    next_i = i

if len(after_x) != N:
    # 「全ての文字列がT」ではない
    # 残りの文字列について操作する（最初のTは処理したので、必ずSから始まる）
    for i, char in enumerate(X[next_i:]):
        if i == 0:
            # 最初は確定でSから始まる
            s_count += 1
            continue

        if char == "S":
            # Sの場合
            if X[next_i + i - 1] == "T":
                # T->Sの切り替わりのとき
                if t_count >= s_count:
                    # Sを全て使い切り、余ったTは確定で残る
                    after_x += "T" * (t_count - s_count)
                    t_count = 0
                    s_count = 0
                else:
                    # Tを全部使い切り、余ったSは引き継がれる
                    s_count -= t_count
                    t_count = 0
            s_count += 1
        else:
            # Tの場合
            t_count += 1
    last_char = char

    if last_char == "T":
        # Tで終わる場合
        if t_count >= s_count:
            # Sを全て使い切り、余ったTは確定で残る
            after_x += "T" * (t_count - s_count)
            t_count -= s_count
            s_count = 0
        else:
            # Tを全部使い切り、余ったSは引き継がれる
            s_count -= t_count
            t_count = 0
            after_x += "S" * s_count
    else:
        # Sで終わる場合
        after_x += "S" * s_count
# print(after_x)
ans = len(after_x)
print(ans)
