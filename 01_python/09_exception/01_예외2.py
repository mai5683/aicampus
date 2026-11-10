"""
예외 처리 (Exception Handling)

예외 상황이 안 생기게 할 수는 없으니 Plan B를 미리 준비해 두자.
"""


# (ex) 1/N 계산기

try :  # Plan A : 최상의 결과
    price = int(input("술값 : "))
    people = int(input("인원 : "))

    money = price // people
    change = price % people

    print("1인당 :", money)
    print("남은 돈 :", change)

except ZeroDivisionError :  # Plan B-1 (인원수에 0을 입력했을 때)
    print("인원수는 0일 수 없습니다")
except ValueError :  # Plan B-2 (잘못된 입력 떄)
    print("잘못된 입력값입니다")