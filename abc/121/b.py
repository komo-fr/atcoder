# https://atcoder.jp/contests/abc121/tasks/abc121_b
# B - Can you solve this?

n, m, c = list(map(int, input().split()))
b_list = list(map(int, input().split()))
a_list_list = []

for _ in range(n):
    a_list = list(map(int, input().split()))
    a_list_list.append(a_list)

count = 0

for a_list in a_list_list:
    total = sum([a * b for a, b in zip(a_list, b_list)]) + c
    if total > 0:
        count += 1

print(count)
