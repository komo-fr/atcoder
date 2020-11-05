# https://atcoder.jp/contests/abc124/tasks/abc124_c
# C - Coloring Colorfully

s = input().split()[0]

pat_1_list = []
pat_2_list = []

for i in range(len(s)):
    if i % 2 == 0:
        pat_1_list.append('0')
        pat_2_list.append('1')
    else:
        pat_1_list.append('1')
        pat_2_list.append('0')

change_count_list = []

for pat_list in [pat_1_list, pat_2_list]:
    # print('pat_list: {}'.format(pat_list))
    change_count = 0
    for pat_char, s_char in zip(pat_list, s):
        if pat_char != s_char:
            change_count += 1
    change_count_list.append(change_count)

# print(change_count_list)
ans = min(change_count_list)

print(ans)