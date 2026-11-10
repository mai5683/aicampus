"""
함수는 데이터를 반환할 수 있습니다

1. 곱셈을 처리하는 함수 - mul()
2. 제곱을 처리하는 함수 - square()

1, 2번을 이용해서 원의 넓이를 구해보자!

(반환값1의 문제점) 출력만 하고 끝나니까 값을 얻어내서 추가계산이 불가하다.
"""

# 곱하기만 하고 출력은 하지 않도록 변경
# 출력을 안 하면 어떻게 해? → 값만 토해내라 (=반환하라, return)
def mul(left,right):
    result = left * right
    return result

def square(number):
    # result = number * number
    result = number ** 2
    return result

# --------------------------------
# main
# --------------------------------

# 원의 넓이 = 반지름² * 원주율(3.14)
# a = square(5)
# b= mul(a, 3.14)
# print(a, b)

# circle = square(5) * 3.14
# print(circle)

circle = mul(square(5), 3.14)
print(circle)