a, b, c = list(map(int, input().split()))
s_list = list(input().split())
t_list = list(input().split())
u_list = list(input().split())

ans = len(set(u_list) - set(s_list + t_list))
print(ans)
