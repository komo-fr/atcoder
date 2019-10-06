# https://atcoder.jp/contests/abc111/tasks/arc103_a
# C - /\/\/\/
import collections

n = int(input().split()[0])
v_list = list(map(int, input().split()))

# 奇数番目の数
odd_list = [str(v) for i, v in enumerate(v_list) if i % 2 == 1]
# 偶数番目の数
even_list = [str(v) for i, v in enumerate(v_list) if i % 2 == 0]

# 奇数の最頻値（No1とNo2)
odd_counter = collections.Counter(odd_list)
odd_1 = odd_counter.most_common()[0][0]

if len(odd_counter) >= 2:
    odd_2 = odd_counter.most_common()[1][0]
else:
    odd_2 = '*' # dummy

# 偶数の最頻値（No1とNo2)
even_counter = collections.Counter(even_list)
even_1 = even_counter.most_common()[0][0]

if len(even_counter) >= 2:
    even_2 = even_counter.most_common()[1][0]
else:
    even_2 = '+' # dummy

# 以前の方法だと条件分岐が複雑になるので
# とりうる操作を全部試して、回数が少ない方をとる

if even_1 == odd_1:
    # 偶数側の操作回数（最頻値で置き換え）
    even_op_count = len([v for v in even_list if v != even_1])
    # 奇数の操作回数
    odd_op_count = len([v for v in odd_list if v != odd_2])
    count_1 = even_op_count + odd_op_count

    # 偶数側の操作回数
    even_op_count = len([v for v in even_list if v != even_2])
    # 奇数側の操作回数（最頻値で置き換え）
    odd_op_count = len([v for v in odd_list if v != odd_1])
    count_2 = even_op_count + odd_op_count

    count = min(count_1, count_2)
else:
    # 偶数側も奇数側も最頻値で置き換えればよい
    even_op_count = len([v for v in even_list if v != even_1])
    odd_op_count = len([v for v in odd_list if v != odd_1])
    count = even_op_count + odd_op_count

print(count)
