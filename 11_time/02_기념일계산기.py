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



from datetime import datetime, timedelta

user = input("날짜 입력(YYYY-MM-DD) : ")
years = int(input("몇 년까지 계산할까요? : "))
date = datetime.strptime(user, "%Y-%m-%d")

dates = []

for i in range(1, (years * 365) // 100 + 1):
    result100 = date + timedelta(days=100 * i)
    dates.append((100 * i, result100))

for i in range(1, years + 1):
    result365 = date + timedelta(days=365 * i)
    dates.append((365 * i, result365))

dates.sort()

for day in dates:
    print(f"D + {day[0]} : {day[1].strftime('%Y-%m-%d')}")





