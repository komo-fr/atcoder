import itertools

s = input().split()[0]
hatena_index_list = []
not_hatena_dict = {}
for i, char in enumerate(s):
    if char == '?':
        hatena_index_list.append(i)
    else:
        not_hatena_dict[i] = char
max_s = int(s.replace('?', '9'))
# print('max')
# print(max_s)
cnt = 0
kouho_list = []
while True:
    work = 5 + 13 * cnt
    cnt += 1
    if work > max_s:
        break
    kouho_list.append(work)

# print('kouho_list: {}'.format(len(kouho_list)))
match_list = []
for kouho in kouho_list:
    kouho_str = str(kouho).zfill(len(s))
    is_ok = True
    for key, value in not_hatena_dict.items():
        if kouho_str[key] == value:
            pass
        else:
            is_ok = False
            break
    if is_ok:
        match_list.append(kouho)

match_list = list(set(match_list))
cnt = len(match_list)
answer = cnt % (10**9 + 7)
print(answer)
