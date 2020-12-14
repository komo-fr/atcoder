#!/usr/bin/env python3
from collections import namedtuple, defaultdict

N, W = list(map(int, input().split()))
Item = namedtuple("Item", ["s", "t", "p"])
item_list = []
s_map = defaultdict(lambda: [])
min_s = float("inf")
max_t = -float("inf")

for _ in range(N):
    s, t, p = list(map(int, input().split()))
    min_s = min([min_s, s])
    max_t = max([max_t, t])
    s_map[s].append(Item(s, t, p))

w_list = [0 for _ in range(max_t + 1)]
is_ok = True
for s_i in range(min_s, max_t + 1):
    # print(f"{s_i=}")
    if min_s != 0:
        w_list[s_i] = w_list[s_i - 1] + w_list[s_i]
    items = s_map[s_i]
    # print(f"{items=}")
    for item in items:
        # print(item)
        w_list[item.s] += item.p
        w_list[item.t] -= item.p
    w = w_list[item.s]
    if w > W:
        is_ok = False

# print(f"{w_list=}")
ans = "Yes" if is_ok else "No"
print(ans)
