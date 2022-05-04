#!/usr/bin/env python
# coding: utf-8

# In[19]:


# in 문자열 연산자를 활용하여 짝수와 홀수를 구분

# 입력을 받습니다.
num = input("정수 입력> ")
last_num = num[-1]

# 짝수 조건
if last_num in '02468':
    print("짝수입니다")

# 홀수 조건
if last_num in '13579':
    print("홀수입니다")

