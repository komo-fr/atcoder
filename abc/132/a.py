# https://atcoder.jp/contests/abc132/tasks/abc132_a
# A - Fifty-Fifty

s = input().split()[0]
count_dict = {}

for char in list(s):
    if char in count_dict.keys():
        count_dict[char] += 1
    else:
        count_dict[char] = 1

ans = True

if len(count_dict.keys()) == 2:
    is_match = True
    for k, v in count_dict.items():
        if v != 2:
            is_match = False
else:
    is_match = False

ans = 'Yes' if is_match else 'No'

print(ans)