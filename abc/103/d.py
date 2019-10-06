# https://atcoder.jp/contests/abc103/tasks/abc103_d
# D - Islands War

n, m = list(map(int, input().split()))
ab_list = []

for _ in range(m):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))

# bの1個前なら絶対切れる
ab_list = sorted(ab_list, key=lambda x: (x[1]))
# print(ab_list)
i = 0
count = 0

while i < len(ab_list):
    count += 1

    a, b = ab_list[i]
    diff_index = 1
    end_index = b

    debug_list = [(a, b)]

    if (i + diff_index) >= len(ab_list):
        break

    # 次の区間について
    while ab_list[i + diff_index][0] < end_index:
        # debug_list.append(ab_list[i + diff_index])

        diff_index += 1

        if (i + diff_index) >= len(ab_list):
            break

        # if ab_list[i + diff_index][1] < end_index:
        #     end_index = ab_list[i + diff_index][1]

    # print('==========')
    # print(debug_list)

    i = i + diff_index

print(count)
