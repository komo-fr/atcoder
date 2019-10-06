N = int(input().split()[0])
b_list = list(map(int, input().split()))

a_list = []

for i in range(N):
    if i == 0:
        a = b_list[0]
        a_list.append(a)
        continue
    if i == N - 1:
        a = b_list[i-1]
        a_list.append(a)
        continue

    # BiとBi-1以下である必要がある
    a = min(b_list[i-1], b_list[i])
    a_list.append(a)

ans = sum(a_list)
print(ans)
