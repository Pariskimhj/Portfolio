#!/usr/bin/env python
# coding: utf-8

# In[4]:


list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")
del list_a[1]  #del list명[인덱스]
print("del list_a[1]:",list_a)
list_a.pop(2)  #list명.pop(인덱스)
print("pop(2):", list_a)

