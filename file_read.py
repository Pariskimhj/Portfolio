#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 파일 열기
with open("basic.txt","r") as file:
    # 파일 읽고 출력
    contents = file.read()
print(contents)

