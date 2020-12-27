#!/usr/bin/env python3
from collections import defaultdict, Counter
import itertools

N, M = list(map(int, input().split()))
abc_list = []
abc_set_list = []

for _ in range(M):  # 364
    a, b, c = list(map(int, input().split()))
    abc = list(sorted([a, b, c]))
    abc_set_list.append((a, b, c))

patterns = list(itertools.product([True, False], repeat=N))
max_count = 0
for pattern in patterns:  # O(16384)
    is_ok = True  # 成立する
    after_list = abc_set_list[:]
    drug_list = []
    # print(f"========================")

    for i, flag in enumerate(pattern):  # O(14)
        if not flag:
            # この薬は使わない
            continue
        drug_id = i + 1
        drug_list.append(drug_id)
        next_list = []
        # print(f"薬{drug_id}を使う.")
        for j in range(M):  # O(364)
            w_list = list(after_list[j])
            # print(f"{j}: {w_list}")
            if drug_id in w_list:
                w_list.remove(drug_id)  # O(364)
                if not w_list:  # 3つ全部使ってしまった
                    # 爆発
                    is_ok = False
                    break
            # 爆発しなかった
            next_list.append(w_list)
        after_list = next_list
        if not is_ok:
            # 爆発したので考慮しない
            break

    if is_ok:
        count = 0
        out_list = []
        for a in after_list:
            if len(a) == 1:
                out_list.append(a[0])
                # count += 1
        count = len(set(out_list))
        max_count = max([max_count, count])


ans = max_count
print(ans)
