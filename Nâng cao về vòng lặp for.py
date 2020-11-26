# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 23:44:09 2020

@author: pc
"""

list2 = [({'name': 'Peter', 'age':2}, {'name': 'John', 'age':21}), 
         ({'name': 'Mary', 'age':2}, {'name': 'Trandanpro', 'age':21}), 
         ({'name': 'Nam', 'age':2}, {'name': 'Hung', 'age':21}), 
         ({'name': 'Mai', 'age':2}, {'name': 'Loan', 'age':21})]
for i in list2:
   #print(i)
   for x in i :
     print(x)
     for count,y in enumerate(x,1):
       print(count,y,":",x[y])
    