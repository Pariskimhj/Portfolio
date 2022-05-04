#!/usr/bin/env python
# coding: utf-8

# In[10]:


# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 출력합니다.
print("{} 년\n{} 월\n{} 일\n{} 시\n{} 분\n{} 초\n".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

