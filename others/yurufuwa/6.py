import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.sparse.csgraph import dijkstra

n = int(input().split()[0])
adj = np.zeros([n, n])

for _ in range(n):
    temp = list(map(int, input().split()))
    if len(temp) == 1:
        q = temp[0]
        break
    u, v, c = temp
    adj[u - 1][v - 1] = c
    adj[v - 1][u - 1] = c

d_matrix, path = dijkstra(adj, return_predecessors=True)
t = 0
mod = 10 ** 9 + 7
ans_list = []
for _ in range(q):
    m, p, x = list(map(int, input().split()))
    # mpx_list.append(dict(m=m, p=p, x=x))
    # adjはnumpy配列
    t = x * d_matrix[m - 1][p - 1]
    temp = int(t) % mod
    ans_list.append(temp)

ans = "\n".join([str(x) for x in ans_list])
print(ans)
