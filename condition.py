#!/usr/bin/env python
# coding: utf-8

# In[28]:


# 입력을 받습니다.
number = input("정수 입력> ")
number = int(number)

# 양수 조건
if number > 0:
    print("양수입니다")
elif number < 0:
    print("음수입니다")
else:
    print("0입니다")

