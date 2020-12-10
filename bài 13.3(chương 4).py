# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:16:21 2020

@author: tanta
"""

import random
import string
#13.1.1: Nhập dung lượng dữ liệu giới hạn là  1MB <= size <= 1024MB.
dulieu=int(input('nhập giới hạn dữ liệu(MB)= '))
while (dulieu<1 or dulieu>1024):
	dulieu = int(input('nhập lại giới hạn dữ liệu (1->1024MB)= '))
#13.1.2: Giới hạn dung lượng mỗi file là  1000KB.
t=1000*1024 
a= dulieu*(2**20)//(t) 
b= dulieu*(2**20)%(t)
#13.3.3: Hãy sinh dữ liệu ngẫu nhiên kiểu chuỗi và lưu vào file
f= string.ascii_lowercase*48733
def text(): 
    c=''.join(random.sample(f,t))
    return c
print('số file có kích thước 1000KB là: ',a)
print('file cuối cùng có kích thước: ',b/1024,"KB")
for i in range(a): 
	file=open('tantai'+str(i+1)+'.txt' ,'x')
	file.write(text())
	file.close()
if b>0: 
    file=open('proboy'+'.txt' ,'x')
    file.write(''.join(random.sample(f,b)))
file.close()
print('Kết thúc')