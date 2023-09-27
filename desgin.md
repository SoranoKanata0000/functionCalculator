## 変数込みの計算
- sympyを使用
- 
  
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

### 