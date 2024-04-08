#!/usr/bin/env python3
import itertools

N = int(input().split()[0])
a_list = list(map(int, input().split()))
b_n = 3 * N  # 棒の数
"""
- 総当たりが可能か考える
- 3*N個のものを3本1組にするパターンは何通りあるか
- 3*Nから3個選ぶ C(3*N, 3)
- 3*(N-1)から3個選ぶ C(3N-3, 3)
- ...
- 3*1から3個選ぶ C(3, 3)
- Maxで369600通り
"""
index_list = list(range(3*N))

p_list = []
# 最初の3個
patterns = itertools.combinations(index_list, 3)
for p1 in patterns:
    p1 = frozenset(p1)
    if N >= 2:
        # 選んだやつ以外から3個選ぶ
        index_list_2  = index_list.copy()
        for i in p1:
            index_list_2.remove(i)
        patterns_2 = itertools.combinations(index_list_2, 3)
        for p2 in patterns_2:
            p2 = frozenset(p2)
            if N >= 3:
                index_list_3  = index_list_2.copy()
                for i in p2:
                    index_list_3.remove(i)
                patterns_3 = itertools.combinations(index_list_3, 3)
                for p3 in patterns_3:
                    p3 = frozenset(p3)
                    if N>=4:
                        index_list_4 = index_list_3.copy()
                        for i in p3:
                            index_list_4.remove(i)
                        patterns_4 = itertools.combinations(index_list_4, 3)
                        for p4 in patterns_4:
                            p4 = frozenset(p4)
                            p_list.append(frozenset([p1, p2, p3, p4]))
                    else:
                        p_list.append(frozenset([p1, p2, p3]))
            else:
                p_list.append(frozenset([p1, p2]))
    else:
        p_list.append(frozenset([p1]))

p_list = set(p_list)
count = 0
# print("🐥", p_list)
ans_list = []
for pattern in p_list:
    is_ok = True
    # print("🍎", pattern)
    for index_tuple in pattern:
        # print("🐳", index_tuple)
        x_list = [a_list[i] for i in index_tuple]
        x_list.sort()
        if x_list[0] + x_list[1] <= x_list[2]:
            is_ok = False
            break
    if is_ok:
        count += 1
        ans_list.append(pattern)

ans = count
print(ans)
