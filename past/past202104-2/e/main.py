#!/usr/bin/env python3

N = int(input().split()[0])
S = input()
node_dict = {}
head_id = None
tail_id = None
length = 0

def print_list(node_dict, head_id):
    cur_node_id = head_id
    data_list = []
    data_list.append(cur_node_id)
    while cur_node_id:
        cur_node_id = node_dict[cur_node_id][1]
        data_list.append(cur_node_id)
    print(str(data_list) + f"{head_id=}, {tail_id=}")

for i, char in enumerate(S):
    # print(node_dict)
    # print_list(node_dict, head_id)
    # print("=================")
    # print(f"{i=}, {char=}")
    node_id = i + 1
    

    if char == "L":
        if length != 0:
            # 現在の先頭を更新
            # print(f"現在の先頭を更新: {node_dict[head_id]} -> ({node_id}, {node_dict[head_id][1]})")
            node_dict[head_id] = (node_id, node_dict[head_id][1])
        else:
            tail_id = node_id
        # 先頭に追加
        node_dict[node_id] = (None, head_id)
        # 先頭を更新
        head_id = node_id
        length += 1
    elif char == "R":
        if length != 0:
            # 現在の末尾を更新
            # print(f"現在の末尾を更新: {node_dict[tail_id]} -> ({node_dict[head_id][0]}, {node_id})")
            node_dict[tail_id] = (node_dict[tail_id][0], node_id)
        else:
            head_id = node_id
        # 末尾に追加
        node_dict[node_id] = (tail_id, None)
        # 末尾を更新
        tail_id = node_id
        length += 1
    elif char in "ABCDEF":
        n = dict(A=1, B=2, C=3, D=1, E=2, F=3)[char]
        if length < n:
            print("ERROR")
            continue
        
        if char in "ABC":
            cur_node_id = head_id  # カーソル
        else:
            cur_node_id = tail_id  # カーソル
        
        for index in range(1, n+1):
            # print(f"{cur_node_id=}")
            if index == n:
                # 取り除く
                # print(f"{cur_node_id}を削除!")
                print(cur_node_id)
                length -= 1  # 長さを減らす

                # 連結リストの更新
                pre_id, next_id = node_dict[cur_node_id]
                # print(f"更新対象のノード {pre_id=}, {next_id=}")

                if pre_id is None:
                    # 直前にノードがない場合、先頭を更新
                    head_id = next_id
                else:
                    # 直前のノードを更新
                    node_dict[pre_id] = (node_dict[pre_id][0], next_id)
                if next_id is None:
                    # 直後にノードがない場合、末尾を更新
                    tail_id = pre_id
                else:
                    # 直後のノードを更新
                    # print(f"debug: node_dict[next_id][0]={node_dict[next_id][0]}")
                    node_dict[next_id] = (pre_id, node_dict[next_id][1])
            else:
                # カーソルを進める
                if char in "ABC":
                    cur_node_id = node_dict[cur_node_id][1]
                else:
                    cur_node_id = node_dict[cur_node_id][0]
