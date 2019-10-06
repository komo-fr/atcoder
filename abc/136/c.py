# n = int(input().split()[0])
# s = input().split()[0]
# a_list = list(map(int, input().split()))
# s_list = []
# for _ range(0, n):
#     s_list.append(input().split()[0])

n = int(input().split()[0])
h_list = list(map(int, input().split()))

is_ok = True
before_n = 0
kotae_list = []

for i, h in enumerate(h_list[:-1]):
    if h_list[i] <= h_list[i+1]:
        # OK. 何も操作しなくてもクリアできる
        # 1つさげても前回値を下回らないなら、下げといた方がよい
        if before_n <= h_list[i] - 1:
            before_n = h_list[i] - 1

        else:
            # 下げれないときはそのまま
            before_n = h_list[i]
        kotae_list.append(before_n)
        continue
    else:
        if before_n <= h_list[i] - 1:
            # 1つさげても前回値を下回らないなら、下げることでクリアできる可能性がある
            if h_list[i] - 1 <= h_list[i+1]:
                # OK
                before_n = h_list[i] - 1
                kotae_list.append(before_n)
                continue
            else:
                # NG
                # 1つ下げたとしたもクリアできないのでダメ
                is_ok = False
                break
        else:
            # クリアできる可能性がない
            is_ok = False

# print('->'.join([str(x) for x in kotae_list]))

ans = 'Yes' if is_ok else 'No'
print(ans)
