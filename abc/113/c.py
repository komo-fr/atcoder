# https://atcoder.jp/contests/abc113/tasks/abc113_c
# C - ID

n, m = list(map(int, input().split()))
py_list = []

for _ in range(m):
    p, y = list(map(int, input().split()))
    py_list.append((p, y))

sorted_py_list = sorted(py_list, key=lambda x: (x[0], x[1]))

p_no = sorted_py_list[0][0]
y_index = 1
no_dict = {}

for i, py in enumerate(sorted_py_list):
    p, y = py

    if p != p_no:
        p_no = p
        y_index = 1

    no = str(p).zfill(6) + str(y_index).zfill(6)
    no_dict[(p, y)] = no
    y_index += 1

print_list = []

for p, y in py_list:
    print_list.append(no_dict[(p, y)])

ans = '\n'.join(print_list)
print(ans)
