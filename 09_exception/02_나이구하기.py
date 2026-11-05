"""
실습 과제
파일명 : 02_나이구하기.py

사용자에게 YYYY-MM-DD 형태의 날짜를 입력 받아 다음을 구하세요.

- 한국 나이 (korean_age)
- 만 나이 (global_age)

한국나이는 연도만으로 계산하며, 만 나이는 연월일 다 필요하지만 계산 편의상 연도와 월 정보만 추출해서 계산하도록 변경하겠습니다. 만 나이는 12개월당 한 살인걸로 간주합니다.

프로그램에서 발생하는 예외 상황들이 모두 처리될 수 있도록 코드를 구현하세요.
"""

# 만 나이 : 년도 +12개월


import re


birth = input("생년월일 : ")

regexp = r"^(19[0-9]{2}|20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[01])$"
result = re.fullmatch(regexp, birth)

if result is not None:
    korean_age = 2026 - int(birth[:4]) + 1
    if 11 >= int(birth[5:7]) :
        global_age = korean_age - 1
    else :
        global_age = korean_age - 2

else :
    print("정보 입력이 잘못되었습니다.")