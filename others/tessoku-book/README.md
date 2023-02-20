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