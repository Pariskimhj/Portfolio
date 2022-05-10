#!/usr/bin/env python
# coding: utf-8

# In[21]:


# 랜덤하게 1000명의 키와 몸무게 만들기
# 랜덤한 숫자를 만들기 위해 가져온다

import random
han = list('가나다라마사아사자차카타파하')
with open("info.txt","w+") as file:
    for i in range(1000):
        #랜덤하게 1000개 생성
        name = random.choice(han) + random.choice(han)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write("{}, {}, {}\n".format(han, weight, height))

