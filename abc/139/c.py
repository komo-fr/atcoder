N = int(input().split()[0])
h_list = list(map(int, input().split()))

tentou_list = []

for i in range(N-1):
    if h_list[i] >= h_list[i+1]:
        t = 1
    else:
        t = 0
    tentou_list.append(t)

# 一番長い1はどれか
c = 0
c_list = []

for t in tentou_list:
    if t == 0:
        c_list.append(c)
        c = 0
    else:
        c += 1

if tentou_list:
    if t == 1:
        c_list.append(c)
    ans = max(c_list)
else:
    ans = 0

print(ans)
