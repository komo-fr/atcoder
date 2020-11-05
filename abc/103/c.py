# https://atcoder.jp/contests/abc103/tasks/abc103_c
# C - Modulo Summation

n = int(input().split()[0])
a_list = list(map(int, input().split()))

max_a = max(a_list)

max_amari = max_a - 1
m = max_a * 2 - 1

amari_list = []
shou_list = []

for a in a_list:
    amari_list.append(a - 1)

ans = sum(amari_list)
print(ans)