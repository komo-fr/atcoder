# https://atcoder.jp/contests/abc004/tasks/abc004_3
# C - 入れ替え

N = int(input().split()[0])
n_list = [str(i + 1) for i in range(6)]
p_list = []

# 5 * 6 = 30 で1周する
for n in range(30):
    n_list = [str(i + 1) for i in range(6)]

    for i in range(n):
        l = i % 5
        r = i % 5 + 1
        w = n_list[r]
        n_list[r] = n_list[l]
        n_list[l] = w
    p = ''.join(n_list)
    p_list.append(p)

ans = p_list[(N % 30)]

print(ans)
