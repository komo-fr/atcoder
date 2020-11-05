n = int(input().split()[0])
a_list = list(map(int, input().split()))

ans = 1 / sum([1/x for x in a_list])
print(ans)
