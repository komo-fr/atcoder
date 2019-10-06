#!/usr/bin/env python3

N = int(input().split()[0])
a_list = list(map(int, input().split()))

w_list = [(i+1, n) for i, n in enumerate(a_list)]
w_list = sorted(w_list, key=lambda x: x[1])
w_list = [str(w[0]) for w in w_list]
ans = ' '.join(w_list)
print(ans)
