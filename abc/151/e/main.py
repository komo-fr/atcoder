#!/usr/bin/env python3
import collections
import math

N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))


def C(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


counter = collections.Counter(a_list)
# a_set_list = list(sorted(list(set(a_list))))

a_list = list(sorted(a_list))

for i, a_min in enumerate(a_list):
    # TODO: 前と同じだったら同じだけカウント
    max_index = i + K - 1
    sub_count = 0
    while max_index < N - 1:
        nokori_r = K - 2
        count = C(max_index - i - 1, nokori_r)
        sub_count += count

        max_index += 1
    before_count = sub_count


print(ans)
