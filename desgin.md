
  
## BNFによる定義
### 10進数
<integer> ::= <digit> | <non_zero_digit> <integer>
<digit> ::= 0 | <non_zero_digit>
<non_zero_digit> ::= 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

### 四則演算
<expr>   ::= <term> [ ('+'|'-') <term> ]*
<term>   ::= <factor> [ ('*'|'/') <factor> ]*
<factor> ::= <number> | '(' <expr> ')'
<number> :== [0-9]+

## 流れ
1. input部分から式を受け取る
   1. 入力部分はinputで受け取り（実装済み）
   2. 受け取り結果を保存する手段を実装（ここはJavaScriptでできそう）
2. 受け取った式をPythonに渡す
   1. 保存用ファイルを作っておき、受け取った式はそこを通してやりとりする（式受け取り後、ファイルの内容を削除する）
3. Pythonで解釈＆処理
   1. 受け取った式から、数値部分と文字部分を判別し、型変換
   2. Sympyで処理（関数化）
   3. 戻り値を回答用ファイルに保存
4. 処理結果をページに返して出力
   1. JavaScriptで持ってくることになる


## デザイン
- 黒背景
- 
