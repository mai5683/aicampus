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

# 연월일을 문자열(YYYY-MM-DD) 형태로 받는다
str = input("기준일(YYYY-MM-DD) 입력 : ")

# 날짜 생성
from datetime import date, timedelta, datetime

# 기준일 설정
d_day = datetime.strptime(str, "%Y-%m-%d").date()
print("설정된 기준일", d_day)

# 더해야 하는 날짜들을 계산해서 모두 저장
li = []

period = 2
# 100일 단위 계산
for i in range(100, period*365+1, 100):
    after = d_day + timedelta(days=i)
    li.append(after)

# N주년 먼저 계산 : timedelta가 아니라 연도를 증가
# (주의) 2월 29일은 다음 해가 없기 때문에 선택이 필요 (제거 or 대체)
for i in range(1, period+1):
    try:    # 플랜 A
        after_year = date(d_day.year +i, d_day.month, d_day.day)
        li.append(after_year)
    except Exception:   # 플랜 B (2월 29일)
        # pass
        after_year = date(d_day.year + i, 2, 28)    # 대체 날짜 지정
        li.append(after_year)

li.sort()

# 출력
for d in li:
    print(d)


