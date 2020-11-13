#!/usr/bin/env python3
from collections import Counter
import itertools


N, M, K = list(map(int, input().split()))
s_table = []

for _ in range(N):  # 30
    s_list = list(input())
    s_table.append(s_list)

L = min([N, M])
found = False

for l in range(L, 0, -1):
    # print(f"M-l+2 = {list(range(M - l+2))}")

    for start_i in range(N - l + 1):
        # print(f"N - l  = {list(range(N - l))}")

        for start_j in range(M - l + 1):

            # print(f"{start_j=}")
            # print(f"l*l = {l} * {l}")
            rows = s_table[start_i : start_i + l]
            # for row in rows:
            #     print(row[start_j : start_j + l])
            # print("---------------")
            target = [row[start_j : start_j + l] for row in rows]
            target = list(itertools.chain.from_iterable(target))

            counter = Counter(target)
            # print(f"{target=}")
            # print(counter)
            # print(counter.most_common())
            # print("-------")
            # print(counter.most_common()[0][1])
            max_count = counter.most_common()[0][1]
            # print(f"{l*l}-{max_count}={l*l-max_count} <= {K} ? ")
            if l * l - max_count <= K:
                ans = l
                found = True
                break
        if found:
            break
    if found:
        break

print(ans)
