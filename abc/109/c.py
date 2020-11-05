# https://atcoder.jp/contests/abc109/tasks/abc109_c
# C - Skip
import fractions

n, m = list(map(int, input().split()))
x_list = list(map(int, input().split()))

x_list = sorted(x_list + [m])
work_list = x_list[1:]
diff_list = [b - a for a, b in zip(x_list[:-1], x_list[1:])]

# 差分の最大公約数になるはず
work = diff_list[0]
if len(diff_list) > 1:
    for a in diff_list[1:]:
        work = fractions.gcd(work, a)
d = work

print(d)
