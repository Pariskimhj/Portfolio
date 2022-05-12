#!/usr/bin/env python
# coding: utf-8

# In[3]:


def print_n_times(*values, n=2):
    #n번 반복합니다.
    for i in range(n):
        # values 는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        # 단순한 줄바꿈
        print()
# 함수를 호출합니다.
print_n_times("안녕하세요","즐거운","파이썬 프로그래밍", n=3)

