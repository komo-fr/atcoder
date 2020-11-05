# https://atcoder.jp/contests/abc132/tasks/abc132_c
# C - Divide the Problems

n = int(input().split()[0])
d_list = list(map(int, input().split()))

sorted_d_list = sorted(d_list)

if sorted_d_list[int(n/2)-1] == sorted_d_list[int(n/2)]:
    ans = 0
else:
    abc_max = sorted_d_list[int(n/2)-1]
    arc_min = sorted_d_list[int(n/2)]
    k_min = abc_max + 1
    k_max = arc_min

    ans = k_max - k_min + 1

print(ans)

