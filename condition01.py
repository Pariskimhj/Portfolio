#!/usr/bin/env python
# coding: utf-8

# In[17]:


# 입력을 받습니다.
num = input("정수 입력> ")

# 마지막 자리 숫자를 추출
last_num = num[-1]

# 숫자로 변환하기
last_num_int = int(last_num)

# 짝수 확인
if last_num_int == 0 or last_num_int == 2 or last_num_int == 4 or last_num_int == 6 or last_num_int == 8:
    print("짝수입니다")

# 홀수 확인
if last_num_int == 1 or last_num_int == 3 or last_num_int == 5 or last_num_int == 7 or last_num_int == 9:
    print("홀수입니다")

