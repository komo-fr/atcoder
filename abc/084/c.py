# https://atcoder.jp/contests/abc084/tasks/abc084_c
# C - Special Trains
import math

N = int(input().split()[0])
csf_list = []

for _ in range(N-1):
    c, f, s = list(map(int, input().split()))
    csf_list.append((c, f, s))

x_list = []
total_c_list = []

for start_i in range(N-1):  # N <= 500
    total_c = csf_list[start_i][0] + csf_list[start_i][1]

    for csf in csf_list[start_i+1:]:  # N <= 500
        c, s, f = csf
        total_c = s if total_c < s else total_c
        i = math.ceil((total_c - s) / f)
        total_c = s + f * i + c
    total_c_list.append(str(total_c))

ans = '\n'.join(total_c_list + ['0'])
print(ans)
