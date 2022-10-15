#!/usr/bin/env python3
import numpy as np
from collections import defaultdict, deque

N, Q = list(map(int, input().split()))
q_list = []
d_table = np.zeros((N, N))


def is_connected(start, end, d_table):
    next_deque = deque([start])  # 次の探索対象
    done_dict = defaultdict(lambda: False)
    ok = False
    while len(next_deque) > 0:  # O(E)
        cur = next_deque.popleft()
        if done_dict[cur]:
            # 既に探索済
            continue
        done_dict[cur] = True

        for i, connected in enumerate(d_table[cur - 1]):  # O(N)
            node_id = i + 1
            if not connected:
                # 連結していなかったら飛ばす
                continue
            if node_id == end:
                ok = True
                break
            # 次の探索対象に追加
            next_deque.append(node_id)
        if ok:
            break
    return ok


for _ in range(Q):  # O(Q)
    q, u, v = list(map(int, input().split()))
    if q == 1:
        if d_table[u - 1][v - 1] == 1:
            # エッジを削除
            d_table[u - 1][v - 1] = 0
            d_table[v - 1][u - 1] = 0
        else:
            # エッジを削除
            d_table[u - 1][v - 1] = 1
            d_table[v - 1][u - 1] = 1
    else:
        # 探索
        ok = is_connected(u, v, d_table)
        ans = "Yes" if ok else "No"
        print(ans)
