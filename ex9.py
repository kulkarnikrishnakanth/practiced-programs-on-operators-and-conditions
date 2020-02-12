# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:15:10 2020

@author: DW4
"""

age = int(input("enter age: "))
gender = input("enter gender (M/F): ")
marital_status = input("enter marital status (y/n): ")
if gender == "F":
    if age >= 20 and age <= 30 and marital_status == "y":
        print("she may work in urban areas and also she will work in her husband's city")
    elif marital_status == "n":
        print("she will work only in urban areas")
    else:
        print("she will work only in urban areas")
elif age >= 20 and age <= 30 and gender == "M" and marital_status == "n":
    print("he will work anywhere")
elif age >= 20 and age <= 30 and gender == "M" and marital_status == "y":
    print("he will work mear by home town")
else:
    print("Error")
