# https://atcoder.jp/contests/abc038/tasks/abc038_c
# C - 単調増加

N = int(input().split()[0])
a_list = list(map(int, input().split()))

c = 0
seq = 0
for i in range(1, N):
    if a_list[i - 1] < a_list[i]:
        c += 1 + seq
        seq += 1
    else:
        seq = 0

c += N
print(c)
