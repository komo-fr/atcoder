# https://atcoder.jp/contests/abc102/tasks/arc100_a
# C - Linear Approximation

N = int(input().split()[0])
a_list = list(map(int, input().split()))
min_b = float('inf')
max_a = max(a_list)

work_list = [a - (i + 1) for i, a in enumerate(a_list)]
w = sorted(work_list)[int(N / 2)]
ans = sum([abs(x - w) for x in work_list])
print(ans)
