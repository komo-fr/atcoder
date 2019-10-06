# https://atcoder.jp/contests/abc047/tasks/arc063_a
# C - 一次元リバーシ / 1D Reversi

S = input().split()[0]
before = S[0]
work_list = [S[0]]

for s in S[1:]:
    if s != before:
        work_list.append(s)
        before = s

ans = len(work_list) - 1
print(ans)
