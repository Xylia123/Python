#-*- coding: utf-8 -*-
from calculator3 import numbers_sum, main

def testing_numbers_sum1():
    assert numbers_sum(num1=2, num2=3) == 5
    return "testing_numbers_sum1() passed successfully"

def testing_numbers_sum2():
    assert numbers_sum(num1=-2, num2=13) == 11
    return "testing_numbers_sum2() passed successfully"

print testing_numbers_sum1()
print testing_numbers_sum2()

main()