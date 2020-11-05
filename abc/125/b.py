# https://atcoder.jp/contests/abc125/tasks/abc125_b
# B - Resale

n = int(input().split()[0])
v_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

score_list = []

for v, c in zip(v_list, c_list):
    if v - c > 0:
        score_list.append(v-c)

ans = sum(score_list)
print(ans)
