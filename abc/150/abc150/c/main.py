#!/usr/bin/env python3
import itertools

N = int(input().split()[0])
p_list = list(input().split())
q_list = list(input().split())

pp = itertools.permutations(p_list, N)
pp = list(sorted(["".join(x) for x in pp]))

qp = itertools.permutations(q_list, N)
qp = list(sorted(["".join(x) for x in qp]))

p = "".join(p_list)
q = "".join(q_list)

p_index = qp.index(p)
q_index = qp.index(q)

ans = abs(p_index - q_index)
print(ans)
