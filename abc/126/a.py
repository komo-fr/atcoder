# https://atcoder.jp/contests/abc126/tasks/abc126_a
# A - Changing a Character

n, k = list(map(int, input().split()))
s = input().split()[0]
new_s = list(s)

new_s[k-1] = new_s[k-1].lower()
new_s = ''.join(new_s)
print(new_s)
