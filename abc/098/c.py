# https://atcoder.jp/contests/abc098/tasks/arc098_a
# C - Attention
N = int(input().split()[0])
S = input().split()[0]
min_c = float('inf')
count_dict = {}
now_w = 0
w_count_list = []

for i in range(N):
    w_count_list.append(now_w)
    if S[i] == 'W':
        now_w += 1

now_e = 0
e_count_list = []
r_S = list(reversed(S))
for i in range(N):
    e_count_list.append(now_e)
    if r_S[i] == 'E':
        now_e += 1

e_count_list = list(reversed(e_count_list))

ans = min([w + e for w, e in zip(w_count_list, e_count_list)])
print(ans)
