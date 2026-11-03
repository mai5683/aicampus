"""
함수실습

다음 작업을 수행하는 함수를 만드세요

정수 하나를 전달받아 해당하는 숫자의 구구단을 출력하는 gugudan이라는 함수
"""

# 연습
def multiply(left, right) :
    result = left * right
    print(f"{left} x {right} = {result}")

multiply(2,3)

print("-"*30)

# 구구단함수
def gugudan(number) :
    # for i in range(1,10) :
    #     print(f"{i} x {number} = {i * number}")   --> 이렇게 반복문 활용해도 됨.
    print(f"<구구단 {number}단>")
    print(f"{number} x 1 = {number * 1}")
    print(f"{number} x 2 = {number * 2}")
    print(f"{number} x 3 = {number * 3}")
    print(f"{number} x 4 = {number * 4}")
    print(f"{number} x 5 = {number * 5}")
    print(f"{number} x 6 = {number * 6}")
    print(f"{number} x 7 = {number * 7}")
    print(f"{number} x 8 = {number * 8}")
    print(f"{number} x 9 = {number * 9}")

gugudan(2)
