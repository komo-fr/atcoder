#!/usr/bin/env python3

H, W = list(map(int, input().split()))
a_table = []

for _ in range(H):
    a_list = list(map(int, input().split()))
    a_table.append(a_list)

# dp = [[0] * W for _ in range(H)]
# dp[0][0] = a_table[0][0]
# for h_index in range(H):
#     for w_index in range(W):
#         if h_index == 0 and w_index == 0:
#             continue
#         if h_index == 0:
#             # 最初の行なので、左からくるしかない
#             dp[0][w_index] = dp[0][w_index - 1]
#             continue
#         if w_index == 0:
#             # 左端なので、上からくるしかない
#             dp[h_index][0] = dp[h_index-1][0]
#             continue
#         # それ以外、上と左からくるパターンがある
#         from_left_p = dp[h_index][w_index-1]
#         from_top_p = dp[h_index-1][w_index]
#         if from_left_p >= from_top_p:
#             dp[h_index][w_index] = from_left_p + a_table[h_index][w_index]
#         else:
#             dp[h_index][w_index] = from_top_p + a_table[h_index][w_index]
            
# ans = dp[-1][-1]

# 初期化
dp = []
for _ in range(H):
    dp.append([[0] + [-float("inf")] * (H+W-1) for _ in range(W)])

# dp = [[-float("inf")] * W for _ in range(H)]

def print_table(tables):
    tables = np.array(tables).transpose((2, 0, 1))
    for k, table in enumerate(tables):
        print(k)
        for line in table:
            print(line)


dp[0][0][0] = 0  # 買わない
dp[0][0][1] = a_table[0][0] # 買う

for h_index in range(H):
    for w_index in range(W):
        for k_index in range(H+W-1):
            if h_index == 0 and w_index == 0:
                continue
            if h_index == 0:
                # 最初の行なので、左からくるしかない
                pre_max_value = dp[0][w_index - 1][k_index]
                # 買った場合に、価値を更新できるか？
                kouho_value = pre_max_value + a_table[h_index][w_index]
                if kouho_value > dp[0][w_index-1][k_index+1]:
                    dp[0][w_index][k_index+1] = kouho_value  # 買う
                else:
                    # 価値を更新できないので買わない
                    dp[0][w_index][k_index+1] = dp[0][w_index-1][k_index+1]  # 買わない
                # dp[0][w_index][k_index] = pre_max_value  # 買わない
                continue
            if w_index == 0:
                # 左端なので、上からくるしかない
                pre_max_value = dp[h_index-1][0][k_index]
                # 買った場合に、価値を更新できるか？
                kouho_value = pre_max_value + a_table[h_index][w_index]
                if kouho_value > dp[h_index-1][0][k_index+1]:
                    dp[h_index][0][k_index+1] = kouho_value  # 買う
                else:
                    # 価値を更新できないので買わない
                    dp[h_index][0][k_index+1] = dp[h_index-1][0][k_index+1]  # 買わない
                
                # dp[h_index][0][k_index] = pre_max_value  # 買わない
                continue
            
            # それ以外、上と左からくるパターンがある
            from_left_max_value = dp[h_index][w_index-1][k_index]
            from_top_max_value = dp[h_index-1][w_index][k_index]
            pre_max_value = max([from_left_max_value, from_top_max_value])
            # 買った場合、価値を更新できるか？
            kouho_value = pre_max_value + a_table[h_index][w_index]

            from_left_max_value_k1 = dp[h_index][w_index-1][k_index+1]
            from_top_max_value_k1 = dp[h_index-1][w_index][k_index+1]
            pre_max_value_k1 = max([from_left_max_value_k1, from_top_max_value_k1])

            if kouho_value > pre_max_value_k1:
                dp[h_index][w_index][k_index+1] = kouho_value  # 買わない
            else:
                # 価値を更新できない
                dp[h_index][w_index][k_index+1] = pre_max_value_k1  # 買わない
            # dp[h_index][w_index][k_index+1] = pre_max_value + a_table[w_index][k_index] # 買う
            # dp[h_index][w_index][k_index] = pre_max_value  # 買わない

# print_table(dp)

for x in dp[-1][-1][1:]:
    print(x)
