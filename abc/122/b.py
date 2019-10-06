# https://atcoder.jp/contests/abc122/tasks/abc122_b
# B - ATCoder

s = input().split()[0]
acgt = ['A', 'C', 'G', 'T']

check_list = ['*' if char in acgt else '/' for char in s]
acgt_list = ''.join(check_list).split('/')
answer = max([len(x) for x in acgt_list])
print(answer)
