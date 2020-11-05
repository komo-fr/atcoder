# https://atcoder.jp/contests/abc131/tasks/abc131_a
# A - Security

s = input().split()[0]

is_difficult = False

for i in range(0, len(s)-1):
    if s[i] == s[i+1]:
        is_difficult = True
        break

ans = 'Bad' if is_difficult else 'Good'
print(ans)
