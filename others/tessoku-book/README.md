- 自分の得点状況: https://atcoder.jp/contests/tessoku-book/score

## 2.累積和

|対応目次 | 提出| メモ|
|:-----|:-----|:----- |
|2.1 一次元の累積和(1) | [A06](https://atcoder.jp/contests/tessoku-book/submissions/38993248) | ・LからRまでの累積和は、`Lまでの累積和 - (R-1までの累積和)` を計算する<br> ・R = 先頭の場合は引かないで `Lまでの累積和` |
|2.2 一次元の累積和(2) | [A07](https://atcoder.jp/contests/tessoku-book/submissions/38994470) | ・差分リストを作ってから、差分リストの累積和をとる<br>・差分リストは、`L`で+1 して、`R+1` で-1する<br> ・R = 末尾の場合は-1しない（インデックスが範囲外でエラーになるから） |
|2.3 二次元の累積和(1) | [A08](https://atcoder.jp/contests/tessoku-book/submissions/38995733) | ・二次元の累積和は、横方向の累積和を計算してから縦方向に足す<br>・長方形の和は、 `Z(x1, y1) + Z(x0-1, y0-1) - Z(x1, y0-1) - Z(x0-1, y1) `<br>・x軸とy軸を間違えないようにする（問題文では `(y, x)`） |
|2.4 二次元の累積和(2) | [A09](https://atcoder.jp/contests/tessoku-book/submissions/39036343) | ・差分テーブルを作る（ `(x0, y0)` と `(x1+1, y1+1)` で+1、 `(x0, y1+1)`と `(x1+1, y0)`で-1）<br>・A08同様、二次元の累積和を作る（横方向の累積和を計算してから縦方向に足す）|

## 3.二分探索

|対応目次 | 提出| メモ|
|:-----|:-----|:----- |
|3.1 配列の二分探索 | [A11](https://atcoder.jp/contests/tessoku-book/submissions/39038100) | ・`bisect.bisect_left(リスト, 値)`で値を挿入できるインデックスを取得する（同じ値が複数ある場合は左端）|
|3.2 答えで二分探索 | [A12](https://atcoder.jp/contests/tessoku-book/submissions/39055035) | ・「`f(x)`が単調増加or単調減少する」「`f(x) = N`となるような`x`を求めたい」時は、二分探索が使える<br>・`left=xの下限`, `right=xの上限`で探索する<br>・探索中、各`x`を使って`f(x)`を計算し、欲しい答えの条件を満たすかどうかを確認する|
|3.3 しゃくとり法 | [A13](https://atcoder.jp/contests/tessoku-book/submissions/39077200)（二分探索による解き方） | ・全探索では間に合わない<br>・リストから、条件を満たす（`K <= A1 - A2`を満たす`A2`)値を二分探索で探す<br>・組み合わせの数は、`A2のインデックス - A1のインデックス`で計算できる |
| 同上 | [A13](https://atcoder.jp/contests/tessoku-book/submissions/39077472)（しゃくとり法による解き方） | ・先頭を0からN-1まで1ずつ動かす（A1）<br>・末尾を`前回の末尾`から、`条件を満たすギリギリの値`まで1ずつ動かす（A2）<br>・上記同様、組み合わせの数は`A2のインデックス - A1のインデックス`になる |
| 3.4 半分全列挙 | [A14](https://atcoder.jp/contests/tessoku-book/submissions/39108882) | ・全ての要素について列挙すると間に合わない<br>・半分ずつに分けて列挙し、その結果を組み合わせる（半分全列挙）<br>・全列挙だと`O(N**4)`だったが、半分全列挙にすることで `O(N**2) + O(N**2 * 2logN)` → `O(N**2 * logN)` に減らせる|

# 4. 動的計画法

|対応目次 | 提出| メモ|
|:-----|:-----|:----- |
|4.1 動的計画法の基本 | [A16](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_p) | ・（前から見る方法） `dp[i-1] + a` と `dp[i-2] + b` で小さい方を採用する|
|4.2 動的計画法の復元| [A17](https://atcoder.jp/contests/tessoku-book/submissions/39126289) | ・A16と同じ方法で`dp`を作成<br>・ゴールから辿ってルートを復元する<br>・具体的には、 `dp[i-1] + a`と `dp[i-2] + b`を見て小さい方をルートリストに追加する|
|4.3 二次元のDP（1）: 部分和問題| [A18](https://atcoder.jp/contests/tessoku-book/submissions/39158561) | ・縦方向: 何番目の数字まで考えるか（`N+1`個用意）<br>・横方向: 合計値（`S+1`個用意）<br>・値: `i`番目の数字まで考えた時に、合計値を`j`にすることが可能か（`True`/`False`）<br>・更新方法: `dp[i-1][j]`が `True`なら、`dp[i][j]`と`dp[i][j+a]`は`True`（`i`番目の数字を足さなかったケースと足したケース）|

