# https://atcoder.jp/contests/abc076/tasks/abc076_c
# C - Dubious Document 2

blank_s = input().split()[0]
t = input().split()[0]

matched_index_list = []

for i in range(len(blank_s) - len(t) + 1):
    is_match = True
    for s_char, t_char in zip(blank_s[i:i+len(t)], t):
        if s_char != '?' and s_char != t_char:
            is_match = False
            break

    if is_match:
        matched_index_list.append(i)

if not matched_index_list:
    answer = 'UNRESTORABLE'
else:
    replaced_s_list = []
    for index in matched_index_list:
        replaced_s = list(blank_s)
        replaced_s[index:index+len(t)] = t
        replaced_s = ''.join(replaced_s)
        replaced_s = replaced_s.replace('?', 'a')
        replaced_s_list.append(replaced_s)

    answer = min(replaced_s_list)

print(answer)