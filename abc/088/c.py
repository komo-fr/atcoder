# https://atcoder.jp/contests/abc088/tasks/abc088_c
# C - Takahashi's Information

c_matrix = []
for _ in range(3):
    c_list = list(map(int, input().split()))
    c_matrix.append(c_list)

a_matrix = []
a_list = []
b_list = []
a_list.append(0) # a1
b_list.append(c_matrix[0][0])
b_list.append(c_matrix[0][1])
b_list.append(c_matrix[0][2])
a_list.append(c_matrix[1][0] - b_list[0])
a_list.append(c_matrix[2][0] - b_list[0])

is_ok = True

for i in range(3):
    for j in range(3):
        if a_list[i] + b_list[j] != c_matrix[i][j]:
            is_ok = False
            break

    if not is_ok:
        break

ans = 'Yes' if is_ok else 'No'
print(ans)
