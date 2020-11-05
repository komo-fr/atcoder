# https://atcoder.jp/contests/abc042/tasks/arc058_a
# C - こだわり者いろはちゃん / Iroha's Obsession
import copy

N, K = list(map(int, input().split()))
d_list = list(map(int, input().split()))

# 一番上の桁から見ていく
use_list = list(set(range(10)) - set(d_list))
n_list = [int(x) for x in list(str(N))]

# 各桁ごとに、使える数字を使っているかどうか洗い出す
keta_list = [x in use_list for x in n_list]

def can_update(old_n):
    kouho_n_list = [x for x in use_list if x > old_n]
    if kouho_n_list:
        return True
    else:
        return False

# 一番左に出てくるFalseの桁
k_index = keta_list.index(False) if False in keta_list else -1

if k_index != -1:
    is_ok = False

    for index in range(k_index, -1, -1):
        # 途中桁の場合
        old_n = n_list[index]
        # その桁で使用可能な数字があるか
        if can_update(old_n):
            # その桁で使用可能な数字がある
            kouho_n_list = [x for x in use_list if x > old_n]
            new_n = min(kouho_n_list)
            new_n_list = n_list[:index] + [new_n]
            # 当該桁以降は、使用可能な最小値で構成する
            if index < len(keta_list):
                new_n_list += [min(use_list)] * (len(keta_list) - (index+1))
            ans = int(''.join([str(x) for x in new_n_list]))
            is_ok = True
            break

        if not is_ok:
            # 最大桁を更新する
            new_n = sorted(use_list)[1] if min(use_list) == 0 else min(use_list)
            # 残りの桁を全て、使用可能な最小値で置き換える
            new_n = str(new_n) + str(min(use_list)) * len(keta_list)
            ans = int(new_n)

else:
    # 使える数字だけで構成されているので、そのままでOK
    ans = N

print(ans)
