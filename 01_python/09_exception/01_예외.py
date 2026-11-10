"""
예외(Exception)

실행 중 발생하는 돌발상황

실행이 중지된 경우 결과화면에 Traceback 로그가 출력이 되고
예외의 이름이 나오게 된다.

이 이름을 알아야 처리가 가능하다.
(ZeroDivisionError, ValueError)
"""

# (ex) 1/N 계산기
price = int(input("술값 : "))
people = int(input("인원 : "))

money = price // people
change = price % people

print("1인당 :", money)
print("남은 돈 :", change)