#!/usr/bin/env python3
from collections import defaultdict
import sys


H, W = list(map(int, input().split()))
g_map = []
for _ in range(H):
    g = input()
    g_map.append(g)

N = int(input().split()[0])
S = input()

# 再帰の上限を解除
sys.setrecursionlimit(len(S) * 10)

# DFSを H*W 回繰り返す

# 隣接ノードの情報 key=インデックス（タプル形式）, value=隣接するノードのリスト
neighbor_dict = defaultdict(lambda: [])

# 探索済みのノード情報
step_dict = defaultdict(lambda: {})
# 隣接情報を作る
for h in range(H):
    for w in range(W):
        n_list = []
        if h != 0:
            n_list.append((h - 1, w))  # 真上
            if w != 0:
                n_list.append((h - 1, w - 1))  # 左上
            if w < W - 1:
                n_list.append((h - 1, w + 1))  # 右上

        if h < H - 1:
            n_list.append((h + 1, w))  # 真下
            if w != 0:
                n_list.append((h + 1, w - 1))  # 左下
            if w < W - 1:
                n_list.append((h + 1, w + 1))  # 右下
        if w != 0:
            n_list.append((h, w - 1))  # 左
        if w < W - 1:
            n_list.append((h, w + 1))  # 右
        neighbor_dict[(h, w)] = n_list


def search(index: tuple):
    global step
    global step_dict
    global is_ok
    if is_ok:
        return
    # print(f"{index=}")
    neighbor_list = neighbor_dict[index]
    if not step_dict[index]:
        # 経由済にする
        step_dict[index] = dict(g=g_map[index[0]][index[1]])
        # print(f"{step}: {step_dict[index]['g']}")

    # 最後の文字か
    if len(S) == step + 1:
        is_ok = True
        return
    step += 1
    # print(f"👀次文字: {S[step]}")
    for neighbor_index in neighbor_list:
        if step_dict[neighbor_index]:
            # 経由済の隣接ノードはスキップする
            continue
        # 次の使用文字ではない隣接ノードはスキップする
        neighbor_char = g_map[neighbor_index[0]][neighbor_index[1]]
        # print(f"\t👉次候補:{neighbor_char}({neighbor_index})")
        if neighbor_char != S[step]:
            continue
        search(neighbor_index)
    # step_dict[index]["end"] = step


is_ok = False
for h in range(H):
    for w in range(W):
        start_index = (h, w)
        # print(f"----start({start_index})")
        step = 0
        start_char = g_map[start_index[0]][start_index[1]]
        if start_char != S[step]:
            continue
        search(start_index)
        if is_ok:
            break

ans = "Yes" if is_ok else "No"
print(ans)
