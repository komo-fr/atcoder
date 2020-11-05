# https://atcoder.jp/contests/abc110/tasks/abc110_c
# C - String Transformation
import itertools
import collections

S = input().split()[0]
T = input().split()[0]
st_set_list = []

for s, t in zip(S, T):
    st_set_list.append(''.join([s, t]))

# 重複する組み合わせを排除
st_set_list = list(set(st_set_list))

s_list = [s for s, t in st_set_list]
t_list = [t for s, t in st_set_list]
s_c = collections.Counter(s_list)
t_c = collections.Counter(t_list)
ans = 'Yes' if s_c.most_common()[0][1] == 1 and t_c.most_common()[0][1] == 1 else 'No'
print(ans)
