# https://atcoder.jp/contests/abc103/tasks/abc103_b
# B - String Rotation

s = input().split()[0]
t = input().split()[0]

if set(s) != set(t):
    ans = 'No'
elif s == t:
    ans = 'Yes'
else:
    is_match = False
    for i in range(len(s)):
        part_1 = s[-i-1:]
        part_2 = s[:-i-1]
        # print('{} - {}'.format(part_1, part_2))
        work = part_1 + part_2
        if t == work:
            is_match = True
            break
    ans = 'Yes' if is_match else 'No'

print(ans)