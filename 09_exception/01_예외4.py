"""
강제 예외 처리

파이썬이 인지하지 못하는 예외상황을 코드로 발생시킨다.
(ex) 금액과 인원이 음수인 상황
"""


# (ex) 1/N 계산기

try :  # Plan A : 최상의 결과
    price = int(input("술값 : "))
    if price < 0 :
        # raise ValueError
        raise Exception

    people = int(input("인원 : "))
    if people < 0 :
        # raise ValueError
        raise Exception

    money = price // people
    change = price % people

    print("1인당 :", money)
    print("남은 돈 :", change)

except Exception :  # 통합 Plan B
    print("프로그램에서 오류가 발생했습니다")