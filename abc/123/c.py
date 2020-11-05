# https://atcoder.jp/contests/abc123/tasks/abc123_c
# C - Five Transportations
import copy
import math

n = int(input().split()[0]) # 人数
a = int(input().split()[0]) # 電車の定員
b = int(input().split()[0]) # バスの定員
c = int(input().split()[0]) # タクシーの定員
d = int(input().split()[0]) # 飛行機の定員
e = int(input().split()[0]) # 船の定員

# 貪欲法だと時間内に解けないので、
# 一番きついところを考える
min_cap = min([a, b, c, d, e])

# (i - 1) + (5 - i) = 4
# 4分間は乗れない時間帯がある
ans = math.ceil(float(n) / min_cap) + 4

print(ans)
