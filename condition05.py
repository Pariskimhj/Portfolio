#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구하고
now = datetime.datetime.now()
# 쉽게 사용할 수 있게 월을 변수에 저장합니다.
month = now.month
# 조건문으로 계절을 확인합니다.
if 3 <= month <=5:
    print("현재는 봄입니다.")
elif 6 <= month <= 8:
    print("현재는 여름입니다.")
elif 9 <= month <= 11:
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다.")

