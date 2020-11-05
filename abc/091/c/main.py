#!/usr/bin/env python3

N = int(input().split()[0])
r_list = []
b_list = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    r_list.append((a, b))

blue_dict = {}

for _ in range(N):
    c, d = list(map(int, input().split()))
    b_list.append((c, d))
    blue_dict[(c, d)] = []
    for ab in r_list:
        a, b = ab
        if a < c and b < d:
            blue_dict[(c, d)] += [(a, b)]

    if blue_dict[(c, d)]:
        # y座標が大きい順に並び替え
        blue_dict[(c, d)] = sorted(blue_dict[(c, d)], key=lambda x: x[0], reverse=True)

# x座標が小さい順に並び替え
b_list = sorted(b_list, key=lambda x: x[1])
pair_list = []

for b in b_list:
    kouho_r_list = blue_dict[b]
    if kouho_r_list:
        r = kouho_r_list[0]
        pair_list.append((r, a))

        for k, v in blue_dict.items():
            if r in v:
                v.remove(r)

ans = len(pair_list)
print(ans)
