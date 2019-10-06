# n = int(input().split()[0])
# s = input().split()[0]
# a_list = list(map(int, input().split()))
# s_list = []
# for _ range(0, n):
#     s_list.append(input().split()[0])

a, b, c = list(map(int, input().split()))

nokori = a - b
ans = c - nokori
if ans < 0:
    ans = 0
print(ans)
