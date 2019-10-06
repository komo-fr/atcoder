# https://atcoder.jp/contests/arc061/tasks/arc061_a
# たくさんの数式
import itertools

s = input().split()[0]

start_index = 0

sum_list = []

# 0のとき
sum_list.append(int(s))

# 0以外のとき
for spliter_n in range(1, len(s)):
	# print('spliter_n: {}'.format(spliter_n))

	comb_list = list(itertools.combinations(list(range(0, len(s)-1)), spliter_n))
	# print('comb_list: {}'.format(comb_list))
	
	for comb_set in comb_list:
		s_copy = s
		number_list = []
		comb_set_list = list(comb_set)
		comb_set_list = [-1] + comb_set_list
		# print('comb_set_list: {}'.format(comb_set_list))

		for i, a in enumerate(comb_set_list):

			if a == comb_set_list[-1]:
				# 最後の要素だったら
				s_i = comb_set_list[i]+1
				number_list.append(s[s_i:])
				
			else:
				# 最後の要素じゃなかったら
				s_i, e_i = comb_set_list[i]+1, comb_set_list[i+1]+1
				number_list.append(s[s_i:e_i])

		debug_text = (' + ').join(number_list)
		# print('debug_text = {}'.format(debug_text))

		number_list = [int(x) for x in number_list]
		# print(number_list)
		sum_list.append(sum(number_list))
	# print('------------')

# print(sum_list)
answer = sum(sum_list)
print(answer)
