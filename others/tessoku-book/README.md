- 自分の得点状況: https://atcoder.jp/contests/tessoku-book/score

## 累積和

|対応目次 | 提出| メモ|
|:-----|:-----|:----- |
|2.1 一次元の累積和(1) | [A06](https://atcoder.jp/contests/tessoku-book/submissions/38993248) | ・LからRまでの累積和は、`Lまでの累積和 - (R-1までの累積和)` を計算する<br> ・R = 先頭の場合は引かないで `Lまでの累積和` |
|2.2 一次元の累積和(2) | [A07](https://atcoder.jp/contests/tessoku-book/submissions/38994470) | ・差分リストを作ってから、差分リストの累積和をとる<br>・差分リストは、`L`で+1 して、`R+1` で-1する<br> ・R = 末尾の場合は-1しない（インデックスが範囲外でエラーになるから） |
|2.3 二次元の累積和(1) | [A08](https://atcoder.jp/contests/tessoku-book/submissions/38995733) | ・二次元の累積和は、横方向の累積和を計算してから縦方向に足す<br>・長方形の和は、 `Z(x1, y1) + Z(x0-1, y0-1) - Z(x1, y0-1) - Z(x0-1, y1) `<br>・x軸とy軸を間違えないようにする（問題文では `(y, x)`） |