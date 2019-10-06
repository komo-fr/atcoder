N = int(input().split()[0])
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

p = 0

for i in range(N):
    b_index = a_list[i] - 1
    p += b_list[b_index]
    if i != 0:
        if a_list[i] - 1 == a_list[i-1]:
            c_index = a_list[i] - 2
            p += c_list[c_index]
print(p)
