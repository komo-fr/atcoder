# https://atcoder.jp/contests/abc048/tasks/arc064_a
# C - Boxes and Candies

N, x = list(map(int, input().split()))
a_list = list(map(int, input().split()))

c = 0
for i in range(N-1):
    s = a_list[i] + a_list[i+1]
    if s < x:
        # すでにクリアしているので何もしなくてよい
        continue
    elif s > x:
        # どちらを減らすか？ iとi+1あわせてs-x個分食べれば良い
        # 0の時点を考えると、先にある1を食べれるだけ食べた方が効率が良い
        if s - x < a_list[i+1]:
            a_list[i+1] -= s - x
        else:
            nokori = x - a_list[i+1]
            a_list[i+1] = 0
            a_list[i] -= nokori
        c += s - x

print(c)