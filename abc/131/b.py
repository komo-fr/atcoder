# https://atcoder.jp/contests/abc131/tasks/abc131_b
# B - Bite Eating

n, l = list(map(int, input().split()))

taste_list = []

for i in range(1, n+1):
    taste = l + i - 1
    taste_list.append(taste)

abs_taste_list = [abs(x) for x in taste_list]
target_index = abs_taste_list.index(min(abs_taste_list))
taste_list.remove(taste_list[target_index])
ans = sum(taste_list)
print(ans)
