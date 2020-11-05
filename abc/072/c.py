# https://atcoder.jp/contests/abc072/tasks/arc082_a
# C - Together
import itertools
import collections

n = int(input().split()[0])
a_list = list(map(int, input().split()))

a_op_list = [[a-1, a, a+1] for a in a_list]
a_op_list = itertools.chain.from_iterable(a_op_list)
c = collections.Counter(a_op_list)
max_count = max(c.values())

print(max_count)
