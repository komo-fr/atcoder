# https://atcoder.jp/contests/abc127/tasks/abc127_c
# C - Prison

n, m = list(map(int, input().split()))
lr_list = []

for _ in range(m):
    l, r = list(map(int, input().split()))
    lr_list.append((l, r))

card2canopen_dict = {i: True for i in range(1, n+1)}

# 重ね合わせの区間を調べれば良い気がする
kukan_min, kukan_max = 1, n

for i, lr in enumerate(lr_list):
    l, r = lr[0], lr[1]
    if l >= kukan_min:
        kukan_min = l
    if r <= kukan_max:
        kukan_max = r

if kukan_max < kukan_min:
    ans = 0
else:
    ans = len(range(kukan_min, kukan_max+1))

print(ans)
