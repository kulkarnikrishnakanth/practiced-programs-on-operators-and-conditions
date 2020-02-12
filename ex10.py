# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:38:44 2020

@author: DW4
"""

num = int(input("enter a 4 digit number: "))
number = str(num)
if len(number) == 4:
    print(number[::-1])
else:
    print("you did not entered 4 digit number")