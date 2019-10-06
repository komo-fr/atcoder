# https://atcoder.jp/contests/abc085/tasks/abc085_b
n = int(input().split()[0])
length_list = []
for _ in range(n):
    x = int(input().split()[0])
    length_list.append(x)

print(len(list(set(length_list))))
