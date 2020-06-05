#!/usr/bin/env python3

N = int(input().split()[0])
c_list = list(map(int, input().split()))
Q = int(input().split()[0])
s_list = []

for i in range(Q):
    s = list(map(int, input().split()))
    s_list.append(s)
    # 奇数カードの在庫
odd_min = float("inf")
all_min = float("inf")
for i, c in enumerate(c_list):
    all_min = min(all_min, c)
    if (i + 1) % 2 != 0:
        odd_min = min(odd_min, c)
buy_count = 0
all_diff = 0
odd_diff = 0

for s in s_list:
    ope = s
    if ope[0] == 1:
        card, count = int(ope[1]), int(ope[2])
        zaiko = c_list[card - 1] - all_diff
        zaiko = zaiko if card % 2 == 0 else zaiko - odd_diff
        # print("{}のzaiko: {}".format(card, zaiko))
        if count <= zaiko:
            buy_count += count
            c_list[card - 1] -= count

            all_min = min(all_min, zaiko - count)
            odd_min = min(odd_min, zaiko - count) if card % 2 != 0 else odd_min
    elif ope[0] == 2:
        count = int(ope[1])
        # print("odd_min: {}".format(odd_min))
        if count <= odd_min:
            buy_count += count * (N // 2)
            odd_min -= count
            all_min = min(all_min, odd_min)
            odd_diff += count
    else:
        count = int(ope[1])
        # print("all_min: {}, count={}".format(all_min, count))
        if count <= all_min:
            buy_count += count * N
            all_min -= count
            odd_min -= count
            all_diff += count
    # print(buy_count)

ans = buy_count
print(ans)
