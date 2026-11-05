"""
예외 처리 (Exception Handling)

예외 상황이 안 생기게 할 수는 없으니 Plan B를 미리 준비해 두자.
만약 하나의 Plan B로 모두를 처리하고 싶다면...?
Exception을 사용한다. (예외의 적정 최상위 형태)
"""


# (ex) 1/N 계산기

try :  # Plan A : 최상의 결과
    price = int(input("술값 : "))
    people = int(input("인원 : "))

    money = price // people
    change = price % people

    print("1인당 :", money)
    print("남은 돈 :", change)

except Exception :  # 통합 Plan B
    print("프로그램에서 오류가 발생했습니다")