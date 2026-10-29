"""
BMI 계산하기

몸무게(kg)와 키(cm)를 입력 받아 BMI를 계산하여 출력하세요.
BMI = 몸무게 ÷ 키(m)²

(참고) 파이썬은 제곱을 **로 계산한다.
"""

# 입력
cm = float(input("신장(cm) 입력 : "))
kg = float(input("체중(kg) 입력 : "))

# 연산
m = cm/100
BMI = kg/m**2
print(BMI)

# 출력
# print("BMI : ",BMI)
print("BMI : ", round(BMI,2))