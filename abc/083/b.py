# https://atcoder.jp/contests/abc083/tasks/abc083_b
# B - Some Sums

n, a, b = list(map(int, input().split()))

target_list = []

# まずは全探索
for i in range(1, n+1):
    tmp_sum = sum([int(x) for x in list(str(i))])
    if a <= tmp_sum <= b:
        target_list.append(i)

print(sum(target_list))
