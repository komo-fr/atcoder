n, q = list(map(int, input().split()))

ab_list = []
is_ab = True
done_list = []

# while is_ab:
#     a, b = list(map(int, input().split()))
#     ab_list.append((a, b))
#     done_list.append(a)
#     done_list.append(b)
#     if set(done_list) == set(range(1, n+1)):
#         break

for _ in range(n-1):
    a, b = list(map(int, input().split()))
    ab_list.append((a, b))

px_total_dict = {node_id: 0 for node_id in range(1, n+1)}
for _ in range(q):
    p, x = list(map(int, input().split()))
    px_total_dict[p] += x

ab_list = sorted(ab_list, key=lambda x: x[0])

count_list = [0] * n
next_child_list = []

# 子供ではなく親を覚える方式は？
# parent2children_dict = {i: [] for i in range(1, n+1)}

# for i, ab in enumerate(ab_list):
#     a, b = ab
#     next_child_list.append(b)

#     if i != len(ab_list) - 1 and ab_list[i+1][0] == a:
#         # 次の辺も同じノードが始点だったら
#         continue
#     else:
#         parent2children_dict[a] = next_child_list
#         next_child_list = []

ch2pa_dict = {}

for i, ab in enumerate(ab_list):
    a, b = ab
    ch2pa_dict[b] = a

root_id = list(set(list(range(1, n+1))) - set(list(ch2pa_dict.keys())))[0]
# print('root_id: {}'.format(root_id))

# for i, ab in enumerate(ab_list):
#     a, b = ab
#     next_child_list.append(b)

#     if i != len(ab_list) - 1 and ab_list[i+1][0] == a:
#         # 次の辺も同じノードが始点だったら
#         continue
#     else:
#         parent2children_dict[a] = next_child_list
#         next_child_list = []

# print(parent2children_dict)

for node_id in range(1, n+1):
    # print('node_id: {}'.format(node_id))
    count = px_total_dict[node_id]
    count_list[node_id-1] += count
    if node_id != root_id:
        parent_id = ch2pa_dict[node_id]
        count_list[node_id-1] += count_list[parent_id-1]
    # print(child_list)
    # print(count_list)

ans = ' '.join([str(x) for x in count_list])
print(ans)
