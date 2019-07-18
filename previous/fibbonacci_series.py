# -*- coding: utf-8 -*-

# Program to demonstrate the fibbonacci Series 
# This is program is demonstrated in three different algo
# With recursice O(2^n)
# With iterative O(n^2)
# using the formual O(1)

import math

def find_fibbonacci_seq_rec(n):
    if n < 2:
        return n
    return find_fibbonacci_seq_rec(n-1)+ find_fibbonacci_seq_rec(n-2)
    
    
def find_fibbonacci_seq_iter(n):
    if n<2 :
        return True
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a
    
def find_fibbonacci_seq_form(n):
    sq = math.sqrt(5)
    phi = (1+sq) / 2
    return int(math.floor(phi ** n / sq))
    
def test_find_fib():
    n = 10
    #assert(find_fibbonacci_seq_rec(n)==55)
    #assert(find_fibbonacci_seq_iter(n)==55)
    #assert(find_fibbonacci_seq_form(n)==55)
    
    print find_fibbonacci_seq_rec(n)
    print find_fibbonacci_seq_iter(n)
    print find_fibbonacci_seq_form(n)
    
if __name__ == '__main__':
    test_find_fib()