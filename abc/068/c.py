# https://atcoder.jp/contests/abc068/tasks/arc079_a
# C - Cat Snuke and a Voyage

n, m = list(map(int, input().split()))
ab_list = []

for _ in range(m):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))

ab_dict = {k: [] for k in range(1, m+1)}

# 1と接続している島
via_nodes_1 = set([b for a, b in ab_list if a == 1])
via_nodes_2 = set([a for a, b in ab_list if b == n])

# 積集合があるか
via_nodes = via_nodes_1 & via_nodes_2

if len(via_nodes):
    ans = 'POSSIBLE'
else:
    ans = 'IMPOSSIBLE'

print(ans)
