# https://atcoder.jp/contests/abc129/tasks/abc129_a
# A - Airplane

cost_list = list(map(int, input().split()))

ans = sum(cost_list) - max(cost_list)
print(ans)
