"""
함수는 데이터를 반환할 수 있습니다

1. 곱셈을 처리하는 함수 - mul()
2. 제곱을 처리하는 함수 - square()

1, 2번을 이용해서 원의 넓이를 구해보자!
"""

def mul(left,right):
    result = left * right
    print(f"{left} x {right} = {result}")

def square(number):
    # result = number * number
    result = number ** 2
    print(f"{number}의 제곱 = {result}")

# --------------------------------
# main
# --------------------------------
# mul(3,5)  # 호출
# square(5)           # 호출

# 원의 넓이 = 반지름² * 원주율(3.14)
# result = square(5) * 3.14
# result = mul(square(5), 3.14)
# 위 코드들은 성립하지 않는다
# print(square(5))  # None 이 나옴

square(5)
mul(25, 3.14)
