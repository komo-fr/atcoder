# https://atcoder.jp/contests/abc082/tasks/arc087_a
# C - Good Sequence
import collections

n = int(input().split()[0])
a_list = list(map(int, input().split()))

# 取り除くことはできる
# 追加はできない

counter = collections.Counter(a_list)

c = 0

# x個より小さい値xは完全に取り除くしかない
c += sum([v for k, v in counter.items() if v < k])
# x個ちょうどの値xには何もしない
# x個より多い値xは、値xと個数の差分を数える
c += sum([v - k for k, v in counter.items() if v > k])

print(c)
