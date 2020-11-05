# https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_b
# B - Kleene Inversion

import math

n, k = list(map(int, input().split()))
a_list = list(map(int, input().split()))

w = (10 ** 9) + 7
unit_c = 0

# 1個の中だと
for i, a in enumerate(a_list[:-1]):
    unit_c += len([x for x in a_list[i:] if x < a])

appendix = 0
# print(a_list[-1], a_list[0])
if len(a_list) > 1:
    for a in a_list:
        # 自分より小さいやつの数
        appendix += len([x for x in a_list if x < a])

# 2回以上繰り返す場合
# print('unit_c: {}'.format(unit_c))
# print('appendix: {}'.format(appendix))

# total_tento_1 = unit_c * (k-1)
if k-1 == 1:
    work = 1
elif (k-1) % 2 == 0:
    work = (1 + (k-1)) * ((k-1) / 2)
else:
    mid_index = math.floor((k-1) / 2) + 1
    work = (1 + (k-1)) * math.floor((k-1) / 2)
    work += mid_index

t_1 = ((unit_c % w) * (k % w)) % w
t_21 = appendix % w
t_22 = work % w
t_2 = (t_21 * t_22) % w
ans = int((t_1 + t_2) % w)

# ans = ((unit_c * k) + (appendix * work)) % w
# total_amari = int(total_tento % w)
print(ans)