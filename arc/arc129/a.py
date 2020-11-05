# https://atcoder.jp/contests/arc029/tasks/arc029_1
# A - 高橋君とお肉

n = int(input().split()[0])

# 2個のグループに分ける場合の全ての組み合わせ
# 0か1かのどちらかになる
t_list = []

for _ in range(n):
	t = int(input().split()[0])
	t_list.append(t)

bin_str_list = []

for n_10 in range(n**2):
	bin_str = format(n_10, 'b').zfill(n)
	bin_str_list.append(bin_str)

time_list = []

for bin_str in bin_str_list:
	a_list = []
	b_list = []
	# print('--------')
	# print('t_list: {}'.format(t_list))
	# print('bin_str: {}'.format(bin_str))

	for t, t_group in zip(t_list, bin_str):
		if t_group == '0':
			a_list.append(t)
		else:
			b_list.append(t)

	# print('Group A: {} ({})'.format(sum(a_list), a_list))
	# print('Group B: {} ({})'.format(sum(b_list), b_list))
	time_list.append(max(sum(a_list), sum(b_list)))

# print('=======')
# print(time_list)
answer = min(time_list)
print(answer)
