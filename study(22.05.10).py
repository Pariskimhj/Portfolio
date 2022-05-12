#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 22.05.10 Study


# 1. 계산식('10 + 10'의 형식)을 입력받아 사칙연산을 수행 및 출력하는 프로그램을 작성하시오.
# (조건 1) 특정 문자 입력시 종료가 가능하게 할 것. 예) q 입력시 프로그램 종료
# (조건 2) 가능한 모든 경우의 수에 대해 잘못 입력된 경우
#            다시 입력할 수 있게 하는 과정을 설계할 것. 예) 잘못된 계산식 입력시 다시 입력하게
# (조건 3) 종료하기 전까지 새로운 계산식을 입력받아 반복 수행할 수 있는 프로그램을 작성할 것.
# (조건 4) 한 셀 안에 완전한 프로그램을 작성하여 코드를 복사 및 붙여넣기했을 때 문제없이 돌아가게 할 것.
# (조건 5) 출력 결과에 계산식도 포함되도록 작성할 것.

# 실행 결과 예시)
# 10 * 20 = 200.0

while True:
    input_data = input("계산식 입력 : (10 + 20의 형식) > ").split()
    if input_data[0] in 'ㅂq':
        print("프로그램 종료")
        break
    if len(input_data) != 3:
        continue
    if not input_data[0].isnumeric() or not input_data[2].isnumeric():
        print("숫자를 입력하세요")
        continue
    num_1 = float(input_data[0]);num_2 = float(input_data[2]);buho = input_data[1]
    if buho in '+*-/':
        if buho == '+':
            result = num_1 + num_2
        elif buho == '*':
            result = num_1 * num_2
        elif buho == '-':
            result = num_1 - num_2
        else:
            result = num_1 / num_2
        print("{} {} {} = {}".format(num_1,buho,num_2,result))
    else:
        print("부호 입력 오류(+*-/ 입력)")
        continue


# In[64]:


# 2. 이름과 국어, 영어, 수학 점수를 입력 받아 총점과 평균을 출력하는 프로그램을 작성하시오.
# (조건 1) 텍스트 파일을 만들어 프로그램이 실행될 때마다 작성 및 수정이 가능하게 할 것.
# (조건 2) 특정 문자 입력시 종료가 가능하게 할 것. 예) q 입력시 프로그램 종료
# (조건 3) 가능한 모든 경우의 수에 대해 잘못 입력된 경우
#            다시 입력할 수 있게 하는 과정을 설계할 것. 예) 점수가 2과목만 입력시 다시 입력하게
# (조건 4) 한 사람이 아닌 여러 사람의 이름과 점수를 반복적으로 입력받아서 누적 출력할 수 있게 할 것.
# (조건 5) 한 셀 안에 완전한 프로그램을 작성하여 코드를 복사 및 붙여넣기했을 때 문제없이 돌아가게 할 것.
# (조건 6) 코드에 오류가 생겼을 경우를 대비하여 정상 작동 및 오류 발생시 특정 문구가 출력될 수 있도록 작성할 것.

try:
    student = {}
    while True:
        name = input("이름 입력 (홍길동) > ")
        if name in 'qㅂ':
            break
        while True:
            score = input("국어 영어 수학 점수 입력 > ").split()
            if score[0] in 'qㅂ':
                break
            if len(score) == 3:
                break
            else:
                print("점수 다시 입력")
                continue
        score = [int(data) for data in score if data.isnumeric()]
        score.append(sum(score))
        score.append(sum(score)/len(score))
        student[name] = score
    print("이름\t국어\t영어\t수학\t총점\t평균")
    for key, value in student.items():
        print(key,end='\t')
        for score in value:
            print(score,end='\t')
        print()
except:
    print('error')

