"""
실습 과제 : 달력만들기
파일명 : 03_달력만들기.py

Calendar 클래스를 사용하여 다음 규칙에 맞게 달력을 만들어보세요.

- 사용자에게 연도와 월을 입력받는다
- 입력받은 정보에 해당하는 달의 달력을 보여준다
- 탭키와 엔터를 사용해서 간격을 맞춰서 출력하며, 주가 바뀌면 다음 줄에 출력
- 탭키 효과는 문자열 안에 \t를 사용하면 됩니다.
- 엔터키 효과는 문자열 안에 \n을 사용하면 됩니다.
- 이전 달과 다음 달의 날짜도 모두 출력
- 무조건 6주치의 달력이 나오도록 처리

https://mwpt.mma.go.kr/caisBMHS/gtmd/calendar/caisNormalCalPopup.do


연도 입력 : (2026)
월 입력 : (12)
-------------------------------
       < 2026년 12월 >
-------------------------------
일   월   화   수   목   금   토
29   30   1    2   3    4    5
6    7    8    9   10   11   12
13   14   15   16  17   18   19
20   21   22   23  24   25   26
27   28   29   30  31   1    2
3    4    5    6   7    8    9
-------------------------------
"""



import calendar
from datetime import timedelta

year = int(input("연도 입력 : "))
month = int(input("월 입력 : "))

print("-" * 27 + "\n" + f"\t\t<{year}년 {month}월>\t\t" + "\n" + "-" * 27)

weekdays = ["일", "월", "화", "수", "목", "금", "토"]
print(f"{weekdays[0]}\t{weekdays[1]}\t{weekdays[2]}\t{weekdays[3]}\t{weekdays[4]}\t{weekdays[5]}\t{weekdays[6]}")

cal = calendar.Calendar(firstweekday=6)
month_days = cal.monthdatescalendar(year, month)

day_list = []

for week_days in month_days:
    for day in week_days:
        day_list.append(day)

while len(day_list) < 42:
    next_date = day_list[-1] + timedelta(days=1)
    day_list.append(next_date)

# 7개씩 출력
for i in range(0, 42, 7):
    week = day_list[i:i+7]
    print(f"{week[0].day}\t{week[1].day}\t{week[2].day}\t{week[3].day}\t{week[4].day}\t{week[5].day}\t{week[6].day}")

print("-" * 27)

