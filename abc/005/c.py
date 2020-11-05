# https://atcoder.jp/contests/abc005/tasks/abc005_3
# C - おいしいたこ焼きの売り方

t = int(input().split()[0])
n = int(input().split()[0])
a_list = list(map(int, input().split()))
m = int(input().split()[0])
b_list = list(map(int, input().split()))

is_ok = True

for b in b_list:  # 100
    can_list = [a for a in a_list if b - t <= a <= b]
    if not can_list:
        is_ok = False
        break
    a_list.remove(min(can_list))

ans = 'yes' if is_ok else 'no'
print(ans)
