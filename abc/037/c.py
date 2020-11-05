# https://atcoder.jp/contests/abc037/tasks/abc037_c
# C - 総和

N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))
sum_list = []
s = 0

if N == K:
    s = sum(a_list)
else:
    for i in range(N):
        s += a_list[i]
        sum_list.append(s)

    s = 0
    for i in range(K - 1, N):
        if i == K - 1:
            s += sum_list[i]
        else:
            s += sum_list[i] - sum_list[i - K]

print(s)
