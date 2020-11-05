# https://atcoder.jp/contests/abc081/tasks/arc086_a
# C - Not so Diverse
import collections
N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))

c = collections.Counter(a_list)

# 数がすくないやつから使う
c_list = sorted([v for k, v in c.items()])
ans = sum(c_list[:-K])
print(ans)
