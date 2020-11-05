# https://atcoder.jp/contests/abc122/tasks/abc122_c
# C - GeT AC

n, q = list(map(int, input().split()))
s = input().split()[0]
lr_list = [list(map(int, input().split())) for _ in range(q)]

count_ac_list = [0] * n
for i in range(n-1):
    # print('{}: {}'.format(i, s[i:i+2]))
    if s[i:i+2] == 'AC':
        count_ac_list[i+1] = count_ac_list[i] + 1
    else:
        count_ac_list[i+1] = count_ac_list[i]

count_list = [str(count_ac_list[r-1] - count_ac_list[l-1]) for l, r in lr_list]

print('\n'.join(count_list))
