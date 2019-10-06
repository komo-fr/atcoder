# https://atcoder.jp/contests/abc123/tasks/abc123_a
# A - Five Antennas

import itertools

place_list = []

for _ in range(5):
    place_list.append(int(input().split()[0]))

k = int(input().split()[0])

p = itertools.combinations(place_list, 2)

is_ok = True

for p_1, p_2 in p:
    if abs(p_1 - p_2) > k:
        is_ok = False

ans = 'Yay!' if is_ok else ':('

print(ans)
