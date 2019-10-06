#!/usr/bin/env python3
import copy

N, K = list(map(int, input().split()))
S = input()

sorted_s_list = sorted(list(S))
check_dict = {i: ch for i, ch in enumerate(S)}
s = ""

for new_i in range(len(S)):
    # 残っている文字のリスト
    rest_s_list = sorted(check_dict.items(), key=lambda x: x[1])
    for i, ch in rest_s_list:
        if ch == check_dict[new_i]:  # TODO: ここが変わる
            # 位置を変更しないでOK
            s += ch
            # 使用済
            del check_dict[i]
            break
        else:
            # 置き換える必要があるので、
            # 置き換えられるかどうかのチェックをする

            # 仮に置き換えた場合の新しい文字列を作る
            w_dict = copy.copy(check_dict)
            del w_dict[i]
            w_dict[i] = w_dict[new_i]
            del w_dict[new_i]
            work_suffix = [v for k, v in sorted(w_dict.items())]
            work_s = s + ch + ''.join(work_suffix)

            # オリジナルの文字列から位置が変わった文字がどれだけあるか
            count = 0
            for new, old in zip(work_s, S):
                if new != old:
                    count += 1

            if count <= K:
                # 置き換えられる
                s += ch
                del check_dict[i]
                # 後ろに追い出される
                check_dict[i] = check_dict[new_i]
                del check_dict[new_i]
                break
ans = s

print(ans)
