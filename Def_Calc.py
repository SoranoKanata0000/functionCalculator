'''
借り物の関数たち
'''
#-*- encodint:utf-8 -*-
def expr(s):
    global i
    val = int(term(s))
    while i < len(s) and (s[i] == '+' or s[i] == '-'):
        op = s[i]
        i += 1
        val2 = int(term(s))
        if op == '+':
            val += val2
        else:
            val -= val2

    return val

def term(s):
    global i
    val = int(factor(s))
    while i < len(s) and (s[i] == '*' or s[i] == '/'):
        op = s[i]
        i +=1
        val2 = int(factor(s))
        if op == '*':
            val *= val2
        else:
            val /= val2

    return val

def factor(s):
    global i
    if s[i].isdigit():
        return number(s)
    i += 1
    ret = int(expr(s))
    i += 1
    return ret

def number(s):
    global i
    n = ""
    while i < len(s) and s[i].isdigit():
        n += s[i]
        i += 1
    return n

if __name__=="__main__":
    s = '32*1/(10-2)+(2*2+2)'
    i = 0
    print(expr(s))

