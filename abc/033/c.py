# https://atcoder.jp/contests/abc033/tasks/abc033_c
# C - 数式の書き換え

S = input().split()[0]

item_list = S.split('+')
nonzero_list = [item for item in item_list if '0' not in item]
ans = len(nonzero_list)
print(ans)
