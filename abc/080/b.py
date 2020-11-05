# https://atcoder.jp/contests/abc080/tasks/abc080_b
# B - Harshad Number

n = int(input().split()[0])
n_list = [int(x) for x in str(n)]

answer = 'No'

if n % sum(n_list) == 0:
    answer = 'Yes'

print(answer)
