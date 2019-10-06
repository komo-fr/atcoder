import itertools

s = input().split()[0]
hatena_index_list = []

for i, char in enumerate(s):
    if char == '?':
        hatena_index_list.append(i)

data = '01234566789'
r = len(hatena_index_list)
pattern_list = list(itertools.product(data, repeat=r))
match_list = []

for i, pattern in enumerate(pattern_list):
    work = list(s)
    for i, number in enumerate(pattern):
        target_index = hatena_index_list[i]
        work[target_index] = number

    work = ''.join(work)
    work = int(work)
    if work % 13 == 5:
        match_list.append(work)

match_list = list(set(match_list))
cnt = len(match_list)
answer = cnt % (10**9 + 7)
print(answer)
