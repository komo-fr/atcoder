# https://atcoder.jp/contests/abc129/tasks/abc129_c
# C - Typical Stairs

n, m = list(map(int, input().split()))
a_list = []

for _ in range(m):
    a = int(input().split()[0])
    a_list.append(a)

steps_list = [dict(fx1=True, fx2=True) for _ in range(n + 1)]

for step_index in a_list:
    steps_list[step_index] = dict(fx1=False, fx2=False)

    if step_index < n - 1:
        steps_list[step_index + 1]['fx1'] = False
    if step_index < n - 2:
        steps_list[step_index + 2]['fx2'] = False

steps_list[1]['fx2'] = False
p_count_list = [0] * (n + 1)

# fx段目に登る方法は、（fx-1 + fx-2）方法ある
# ただし、x-1が壊れている場合はfx-2通り
# x-2が壊れている場合はfx-1通り
for i, op in enumerate(steps_list):
    if i == 0:
        p_count_list[i] = 1
        continue

    p_count = 0
    if steps_list[i]['fx1']:
        p_count += p_count_list[i-1]
    if steps_list[i]['fx2']:
        p_count += p_count_list[i-2]

    p_count_list[i] = p_count % 1000000007

# print(p_count_list)
ans = p_count_list[-1]
print(ans)
