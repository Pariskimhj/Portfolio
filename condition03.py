#!/usr/bin/env python
# coding: utf-8

# In[21]:


# 나머지 연산자를 활용하여 짝수와 홀수를 구분

# 입력을 받습니다.
num = int(input("정수 입력> "))

# 짝수 조건
if num % 2 == 0:
    print("짝수입니다")

# 홀수 조건
if num % 2 == 1:
    print("홀수입니다")

