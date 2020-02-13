# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:08:37 2020

@author: DW4
"""

classes_held = 200
classes_attended = int(input("enter number of classes attended: "))
percentage = (classes_attended / classes_held) * 100
if percentage >= 75:
    print("your attendece % is=",percentage,"you are allowed to write the exam")
else:
    print("your attendece % is=",percentage,"you are not allowed to write the exam")