#!/usr/bin/env python3
from collections import defaultdict

N, Q = list(map(int, input().split()))
c_list = list(map(int, input().split()))
q_list = []


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, i):
        if self.parents[i] == i:
            # 自分自身だったらそのまま返す
            return i
        else:
            # 自分の祖先を、自分の祖先の祖先で更新する
            # こうすることで、途中を飛ばすことができる
            self.parents[i] = self.find(self.parents[i])
            return self.parents[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i != j:
            # print("別の家族なので養子に迎える")
            i, j = min(i, j), max(i, j)

            # 別の家族だったら養子に迎える
            self.parents[j] = i


uf = UnionFind(N)
com2counter = defaultdict(lambda: defaultdict(lambda: 0))
# student2com = {idx: idx for idx in range(N)}
com_id = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    # print(f"{q=}")
    print("----------------------")
    print(f"全体: {com2counter=}")
    if q[0] == 1:
        # 合流
        x_idx = q[1] - 1
        y_idx = q[2] - 1
        # 生徒が今いる集団
        com_id_1 = uf.find(x_idx)
        com_id_2 = uf.find(y_idx)
        if com_id_1 == com_id_2:
            # 同じ集団だったら何もしない
            continue
        print(f"統合前: {com_id_1=}, {com_id_2=}")
        # 生徒が所属するクラス
        class_1 = c_list[x_idx]
        class_2 = c_list[y_idx]

        if com2counter[com_id_1]["total"] == 0:
            com2counter[com_id_1]["total"] = 1
            com2counter[com_id_1][class_1] += 1
        if com2counter[com_id_2]["total"] == 0:
            com2counter[com_id_2]["total"] = 1
            com2counter[com_id_2][class_2] = 1

        # 小さい方のコミュニティ
        if com2counter[com_id_1]["total"] <= com2counter[com_id_2]["total"]:
            small_com_id = com_id_1
            big_com_id = com_id_2
        else:
            small_com_id = com_id_2
            big_com_id = com_id_1
        print(
            f"{small_com_id=}({com2counter[small_com_id]['total']}), {big_com_id=},({com2counter[big_com_id]['total']})"
        )

        # 統合
        uf.union(x_idx, y_idx)
        print(f"統合後コピー前({big_com_id}): {com2counter[big_com_id]}")
        for k, v in com2counter[small_com_id].items():
            if k in ["total"]:
                continue
            # 小さい方の集団の情報を大きい方の集団にコピー
            com2counter[big_com_id][k] += com2counter[small_com_id][k]
        print(f"統合後コピー後({big_com_id}): {com2counter[big_com_id]}")

        # 合計を更新
        print(f"合計を更新前: {com2counter[big_com_id]['total']}")
        com2counter[big_com_id]["total"] += com2counter[small_com_id]["total"]
        print(f"合計を更新後: {com2counter[big_com_id]['total']}")

    else:
        x_idx = q[1] - 1
        y_class = q[2]
        target_com_id = uf.find(x_idx)
        student_n = com2counter[target_com_id][y_class]
        print(student_n)
