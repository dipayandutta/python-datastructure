# -*- coding: utf-8 -*-


import stack

def string_reverse(str):
    s = stack.Stack()
    print s
    revStr = ''
    for c in str:
        s.push(c)
        
    while not s.isEmpty():
        revStr += s.pop()
    return revStr
    
def string():
    str = "Hello World"
    op = string_reverse(str)
    print op
    
if __name__ == '__main__':
    string()