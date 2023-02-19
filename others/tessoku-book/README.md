- 自分の得点状況: https://atcoder.jp/contests/tessoku-book/score

|対応目次 | 提出| メモ|
|:-----|:-----|:----- |
|2.1 一次元の累積和(1) | [A06](https://atcoder.jp/contests/tessoku-book/submissions/38993248) | ・LからRまでの累積和は、`Lまでの累積和 - (R-1までの累積和)` を計算する<br> ・R = 先頭の場合は引かないで `Lまでの累積和` |
|2.2 一次元の累積和(2) | [A07](https://atcoder.jp/contests/tessoku-book/submissions/38994470) | ・差分リストを作ってから、差分リストの累積和をとる<br>・差分リストは、`L`で+1 して、`R+1` で-1する<br> ・R = 末尾の場合は-1しない（インデックスが範囲外でエラーになるから） |