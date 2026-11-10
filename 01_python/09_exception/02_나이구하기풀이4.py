"""
# 실습 과제

파일명 : `02_나이구하기.py`

사용자에게 `YYYY-MM-DD` 형태의 날짜를 입력 받아 다음을 구하세요

- 한국 나이 (korean_age)
- 만 나이 (global_age)

한국나이는 `연도`만으로 계산하며, 만 나이는 연월일 다 필요하지만 계산 편의상 `연도`와 `월` 정보만 추출해서 계산하도록 변경하겠습니다. 만 나이는 `12`개월당 한 살인걸로 간주합니다.

> 프로그램에서 발생하는 예외 상황들이 모두 처리될 수 있도록 코드를 구현하세요
"""

# 만나이를 계산하는 함수 (오늘날짜를 구하는 방법은 모르니까 지정)
def calculate_global_age(year, month, day):
    current_year = 2026
    current_month = 11
    current_day = 6
    # 연도를 이용해서 나이를 계산
    age = current_year - year

    # 생일이 지나지 않은 경우 1살을 뺀다
    # - 월이 이번달보다 크면 생일이 지나지 않았다고 본다
    #   (month > current_month)
    # - 월이 이번달과 같으면 일을 비교해서 생일이 지나지 않았는지 판단한다
    #   (month == current_month and day > current_day)
    # if month > current_month or (month == current_month and day > current_day):
    if (month, day) > (current_month, current_day): #튜플(리스트) 비교
        age -= 1

    # 계산된 나이 반환
    return age

# main
import re

try:  # 플랜 A
    birth = input("생년월일(YYYY-MM-DD) 입력 : ")
    # 정규표현식으로 선제검사 후 예외로 이동
    regexp = r"^(19[0-9]{2}|20[0-9]{2})-((02-(0[1-9]|1[0-9]|2[0-9]))|((0[469]|11)-(0[1-9]|1[0-9]|2[0-9]|30))|((0[13578]|1[02])-(0[1-9]|1[0-9]|2[0-9]|3[01])))$"
    result = re.fullmatch(regexp, birth)
    if result is None:  # 형식 불일치
        raise Exception("올바른 날짜 형식이 아닙니다")  # 메세지 추가

    year = int(birth[:4])
    month = int(birth[5:7])
    day = int(birth[8:])
    korean_age = 2026 - year + 1  # 한국 나이
    if korean_age < 1:  # 한국나이 < 1 이면 미래의 날짜를 입력했다고 판단
        raise Exception("미래의 날짜는 입력하실 수 없습니다")

    global_age = calculate_global_age(year, month, day)
    if global_age < 0:  # 만나이 < 0 이면 미래의 날짜를 입력했다고 판단
        raise Exception("미래의 날짜는 입력하실 수 없습니다")

    print(f"한국나이 : {korean_age}세")
    print(f"만나이 : {global_age}세")
except Exception as e:  # 플랜 B
    # print("프로그램상의 오류가 발생했습니다")
    print(f"오류 : {e}")

