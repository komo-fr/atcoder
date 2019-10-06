# https://atcoder.jp/contests/abc036/tasks/abc036_c
# C - 座圧

N = int(input().split()[0])
a_list = []

for _ in range(N):
    a = int(input().split()[0])
    a_list.append(a)

sorted_list = sorted(list(set(a_list)))
map_dict = {}

for lank, b in enumerate(sorted_list):
    map_dict[b] = lank

ans_list = [str(map_dict[a]) for a in a_list]
ans = '\n'.join(ans_list)
print(ans)
