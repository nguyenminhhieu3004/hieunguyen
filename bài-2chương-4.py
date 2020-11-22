# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 23:33:03 2020

@author: ADMIN
"""
n=int(input("nhập vào số lần lặp giải phương trình bậc nhất= "))
a=int(input("a= "))
b=int(input("b= "))
x=-b/a
counter=1
print("x= ",str(x))
A=("có dạng: ax+b=0")
while counter <= n:
    counter=counter+1
    print("a= ",a)
    print("b= ",b)
    print("x= ",x)
    print("chương trình lặp giải phương trình bậc nhất n lần", A)
    