# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:46:06 2020

@author: DW4
"""
num = int(input("enter a value: "))
if num >= 10000:
    first_digit = num % 10
    second_digit = (num % 100) // 10
    third_digit = (num // 100) % 10
    fourth_digit = (num // 1000) % 10
    fifth_digit = (num // 10000)
    sum_of_digits = first_digit + second_digit + third_digit + fourth_digit + fifth_digit
    
    if sum_of_digits > 10:
        first_digit = sum_of_digits % 10
        second_digit = (sum_of_digits % 100) // 10
        sum_of_digits =  first_digit + second_digit
    print(sum_of_digits)
        
    
    