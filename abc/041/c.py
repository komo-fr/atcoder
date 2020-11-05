# https://atcoder.jp/contests/abc041/tasks/abc041_c
# C - 背の順

n = int(input().split()[0])
a_list = list(map(int, input().split()))
data_list = []
for i, a in enumerate(a_list):
    data_list.append((i + 1, a))

data_list = sorted(data_list, key=lambda x: x[1], reverse=True)
id_list = [str(d[0]) for d in data_list]
ans = '\n'.join(id_list)
print(ans)
