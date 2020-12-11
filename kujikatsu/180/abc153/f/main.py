#!/usr/bin/env python3
from collections import defaultdict, deque
import math

N, D, A = list(map(int, input().split()))
x_list = []
x2h_dict = defaultdict(lambda: 0)
max_x = 0
min_x = float("inf")
x_list = []
for _ in range(N):
    x, h = list(map(int, input().split()))
    x2h_dict[x] = h
    max_x = max([max_x, x])
    min_x = min([min_x, x])
    # print(f"i={_}")
    x_list.append(x)

x_deque = deque(list(sorted(x_list)))
# print(f"{min_x=}, {max_x=}")
count = 0
damage_dict = defaultdict(lambda: 0)
# for x in range(min_x, max_x + 1):
#     # 今の場所にいるモンスターを倒すのに何回攻撃が必要か
#     # print(f"now_damage=pre({damage_dict[x-1]}) + 打ち消し({damage_dict[x]})")
#     damage_dict[x] = damage_dict[x - 1] + damage_dict[x]
#     now_hp = x2h_dict[x] - damage_dict[x]
#     # print(f"{x=}, {now_hp=}")
#     if now_hp <= 0:
#         continue
#     c = math.ceil(now_hp / A)
#     count += c
#     # 現在値から+D先まで有効
#     damage = c * A
#     # print(f"damage: {A} * {c} = {damage}")
#     damage_dict[x] += damage
#     damage_dict[x + 1 + 2 * D] -= damage

pre_utikesi_damage = 0
x = x_deque.popleft()
pre_x = -1
uchikeshi_damages = deque([])
while len(x_deque) + 1 > 0:
    # 今の場所にいるモンスターを倒すのに何回攻撃が必要か
    # print(f"now_damage=pre({damage_dict[pre_x]}) + 打ち消し({damage_dict[x]})")
    uchikeshi_damage = 0
    uchikeshi_c = 0
    while uchikeshi_damages:
        past_damage = uchikeshi_damages[0]
        # print(f"{uchikeshi_c=}, {past_damage=}")
        if x >= past_damage["x"]:
            uchikeshi_damage += uchikeshi_damages.popleft()["damage"]
        else:
            # uchikeshi_damages.appendleft(past_damage)
            break
    # print(f"pre_damage={damage_dict[pre_x]}, {uchikeshi_damage=}")
    damage_dict[x] = damage_dict[pre_x] - uchikeshi_damage
    now_hp = x2h_dict[x] - damage_dict[x]
    # print(f"{x=}, {now_hp=}")
    if now_hp <= 0:
        if not x_deque:
            break
        next_monster_x = x_deque.popleft()
        pre_x = x
        x = next_monster_x
        continue
    c = math.ceil(now_hp / A)
    count += c
    damage = c * A
    damage_dict[x] += damage
    uchikeshi_damages.append(dict(x=x + 2 * D + 1, damage=damage))
    if x_deque:
        next_monster_x = x_deque.popleft()
        pre_x = x
        x = next_monster_x

ans = count
print(ans)
