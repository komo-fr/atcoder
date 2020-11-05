# https://atcoder.jp/contests/abc028/tasks/abc028_c
# C - 数を3つ選ぶマン
import itertools

x_list = list(map(int, input().split()))

p_gen = itertools.combinations(x_list, 3)
s_list = []
for p in p_gen:
    s_list.append(sum(list(p)))

s_list = list(set(s_list))
s_list = sorted(s_list, reverse=True)
ans = s_list[2]
print(ans)
