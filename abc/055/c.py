# https://atcoder.jp/contests/abc055/tasks/arc069_a
# C - Scc Puzzle
import math
N, M = list(map(int, input().split()))

c = 0
# 使えるSを全部使えるか
# CがM * 2個いる
if M >= N * 2:
    # Sを全部使う
    c += N
    # 残っているcだけでSccを作れるだけ作る
    c += math.floor((M - N * 2) / 4)
else:
    # Sを使えるだけ使う
    max_pair = math.floor(M / 2)
    c += max_pair

c = int(c)
print(c)
