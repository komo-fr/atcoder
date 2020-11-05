# https://atcoder.jp/contests/abc059/tasks/arc072_a
# C - Sequence
import copy
N = int(input().split()[0])
a_list = list(map(int, input().split()))

w_list_1 = copy.copy(a_list)
w_list_2 = copy.copy(a_list)
c_1, c_2 = 0, 0
s_1, s_2 = 0, 0
c_list = []

for i in range(N):  # 10 ** 5
    # 偶数項を正にする場合
    before = w_list_1[i]
    s_1 += before

    if i % 2 == 0 and s_1 < 0:
        w_list_1[i] += abs(s_1)
        c_1 += abs(s_1)
    elif i % 2 != 0 and s_1 >= 0:
        w_list_1[i] -= abs(s_1+1)
        c_1 += abs(s_1+1)

    s_1 = s_1 - before + w_list_1[i]

    if s_1 == 0:
        a = w_list_1[i]
        w_list_1[i] = a + 1 if a >= 0 else a - 1
        s_1 = 1 if a >= 0 else -1
        c_1 += 1

    # 偶数項を負にする場合
    before = w_list_2[i]
    s_2 += before

    if i % 2 == 1 and s_2 < 0:
        w_list_2[i] += abs(s_2)
        c_2 += abs(s_2)
    elif i % 2 != 1 and s_2 >= 0:
        w_list_2[i] -= abs(s_2+1)
        c_2 += abs(s_2+1)

    s_2 = s_2 - before + w_list_2[i]

    if s_2 == 0:
        a = w_list_2[i]
        w_list_2[i] = a + 1 if a >= 0 else a - 1
        s_2 = 1 if a >= 0 else -1
        c_2 += 1

ans = min([c_1, c_2])
print(ans)
