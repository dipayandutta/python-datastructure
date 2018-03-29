# -*- coding: utf-8 -*-

# Prime number checker 
# First Method uses brute force technique
# Second method users rejecting all the candidate upto the square root of the number 
# Using the Fermet's Theorem

import math
import random

def finding_prime(number):
    
    num = abs(number)
    print num
    if num < 4:
        return True
    for x in range(2,num):
        if num %x == 0:
            return False
    return True
    
def finding_prime_sqrt(number):
    
    num = abs(number)
    if num < 4: 
        return True
    for x in range(2,int(math.sqrt(num))+1):
        if number % x == 0:
            return False
    return True
    
    
def finding_prime_fermet_method(number):
    if number <= 102:
        for a in range(2,number):
            if pow(a,number-1,number) != 1:
                return False
        return True
        
    else:
        for i in range(100):
            a = random.randint(2, number-1)
            if pow(a,number-1,number) != 1:
                return False
        return True
        
def test_prime():
    number1 = 20
    number2 = 27
    
    print finding_prime(number1)
    print finding_prime(number2)
    
    print finding_prime_sqrt(number1)
    print finding_prime_sqrt(number2)
    
    print finding_prime_fermet_method(number1)
    print finding_prime_fermet_method(number2)