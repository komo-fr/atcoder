n, p = list(map(int, input().split()))
c_list = list(map(int, input().split()))
c_list = sorted([c for c in c_list if c <= p], reverse=True)
ans = p - max(c_list) if c_list else p

print(ans)
