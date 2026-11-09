"""
실습 과제 : 기념일 계산기
다음 요구사항에 맞는 기념일 계산기를 구현하세요

사용자가 입력한 연, 월, 일 정보를 토대로 기념일을 순차적으로 출력
(문자열 입력으로 해도 상관없습니다)

연도 입력 : (2026)
월 입력 : (3)
일 입력 : (19)

또는

날짜 입력 : (2026-03-19)

D + 100 : yyyy-MM-dd
D + 200 : yyyy-MM-dd
D + 300 : yyyy-MM-dd
D + 365 : yyyy-MM-dd
D + 400 : yyyy-MM-dd
D + 500 : yyyy-MM-dd
D + 600 : yyyy-MM-dd
D + 700 : yyyy-MM-dd
D + 730 : yyyy-MM-dd


사용자가 입력한 날짜부터 계산해서 100일 단위와 1주년 단위(365일)를 계산해서 가까운 일자부터 출력
처음에는 1년만 보이게 하시고 나중에는 10년 또는 사용자가 원하는 만큼의 연도를 보여주세요
"""

# 날짜 입력 받기
year = 2026
month = 3
day = 19

# 날짜 생성
from datetime import date, timedelta

# 기준일 설정
d_day = date(year, month, day)

print("설정된 기준일", d_day)

# 더해야 하는 날짜들을 리스트로 저장한 뒤 사용
# li = [100, 200, 300, 400, 500, 600, 700]
li = [100, 200, 300, 365, 400, 500, 600, 700]


# 출력은 365의 배수와 아닌 것으로 구분하여 출력
for i in range(100, 701, 100):  # 100부터 701 전까지 100씩 증가
    after = d_day + timedelta(days=i)
    if i % 365 == 0:
        print(f"{i//365}주년", after)
    else:
        print(f"{i}일 뒤", after)