# https://atcoder.jp/contests/abc133/tasks/abc133_c
# C - Remainder Minimization 2019

l, r = list(map(int, input().split()))
count = 0
amari_list = []

for i in range(l, r+1):
    count_j = 0
    for j in range(i+1, r+1):
        amari_list.append(i * j % 2019)
        if count_j == 2019:
            break
        count_j += 1

    if count == 2019:
        break
    count += 1

ans = min(amari_list)
print(ans)
