# https://atcoder.jp/contests/abc054/tasks/abc054_b
# B - Template Matching

n, m = list(map(int, input().split()))

a_list_list = []

for i in range(0, n):
    a_list_list.append(input().split()[0])

b_list_list = []

for i in range(0, m):
    b_list_list.append(input().split()[0])

def is_match(source_list_list, b_list_list, source_start_x):

    for k in range(len(b_list_list)):
        for l in range(len(b_list_list[0])):
            if source_list_list[k][source_start_x + l] != b_list_list[k][l]:
                return False

    return True

# def debug_print(source):
#     print('==============')
#     for row in source:
#         print(row)
#     print('==============')

is_ok = False

# debug_print(b_list_list)

for j in range(0, n-m+1):
    target_a_list_list = a_list_list[j:j+m]
    for i in range(0, n-m+1):
        # debug_print(target_a_list_list)
        if is_match(target_a_list_list, b_list_list, i):
            is_ok = True
            break
    if is_ok:
        break

ans = 'Yes' if is_ok else 'No'

print(ans)
