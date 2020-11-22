#!/usr/bin/env python3
from collections import deque
import bisect

# N, M = list(map(int, input().split()))
h_list = list(map(int, input().split()))
w_list = list(map(int, input().split()))

h_list = list(sorted(h_list))
h_deque = deque(h_list)
w_list = list(sorted(w_list))
w_deque = deque(w_list)

h = h_deque.popleft()
w_index = bisect.bisect_left(w_list, h)

if w_index >= 1:
    # 最小のhより小さいwが存在する
    # 最小のhより小さいwのうちmax以外のものは不要
    for _ in range(0, w_index - 1):
        _ = w_deque.popleft()

w = w_deque.popleft()

min_pre_total = 0
raw_pre_total = 0
before_h = h
h_index = 0
while h_deque:
    # 今見ているh
    h = h_deque.popleft()
    print(f"{h_index}: {h=}")
    h_index += 1
    # このフェーズで操作しなかった場合の最小値
    if_no_op_total = min_pre_total + abs(h - before_h)

    if before_h <= w <= h:
        # 操作可能な場合、操作した場合の最小値を求める
        min_if_op_total = raw_pre_total + abs(h - w)
        print(f"操作可能: {w=} 操作した場合: {min_if_op_total=}")
        if w_deque:
            w = w_deque.popleft()
            while before_h <= w <= h:
                if_op_total = raw_pre_total + abs(h - w)
                min_if_op_total = min(min_if_op_total, if_op_total)
                print(f"操作可能: {w=} 操作した場合: {min_if_op_total=}")

                if w_deque:
                    w = w_deque.popleft()
        # 最小値を更新
        min_pre_total = min([if_no_op_total, min_if_op_total])

    else:
        min_pre_total = if_no_op_total

    # 無操作の場合の合計を更新
    raw_pre_total += abs(h - before_h)
    print(f"{raw_pre_total=}, {min_pre_total=}")
    before_h = h
else:
    if h <= w:
        print(f"操作可能: {w=}")
        if_op_total = raw_pre_total + abs(w - h)
        min_pre_total = min([if_no_op_total, if_op_total])
