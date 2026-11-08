from datetime import date, timedelta

year = int(input("연도 입력 : "))
month = int(input("월 입력 : "))

print("-" *27 + "\n" + f"\t\t<{year}년 {month}월>\t\t" + "\n" + "-" *27)

weekdays = ["일", "월", "화", "수", "목", "금", "토"]
print(f"{weekdays[0]}\t{weekdays[1]}\t{weekdays[2]}\t{weekdays[3]}\t{weekdays[4]}\t{weekdays[5]}\t{weekdays[6]}")

# 입력한 연월의 1일
select_date = date(year, month, 1)

# 일요일을 0으로 시작하도록 요일 계산
week = (select_date.weekday() + 1) % 7

# 이전 달 마지막 날짜
prev_date = select_date - timedelta(days=1)

# 이번 달 마지막 날짜 계산
if month == 4 or month == 6 or month == 9 or month == 11:
    last_day = 30
elif month == 2:
    last_day = 28
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        last_day = 29
else:
    last_day = 31

# 날짜를 저장할 리스트
day_list = []

# 이전 달 날짜 추가
for i in range(week):
    prev_day = prev_date.day - week + i + 1
    day_list.append(prev_day)

# 이번 달 날짜 추가
for i in range(1, last_day + 1):
    day_list.append(i)

next_day = 1

while len(day_list) < 42:
    day_list.append(next_day)
    next_day += 1

for i in range(0, 42, 7):
    week = day_list[i:i+7]
    print(f"{week[0]}\t{week[1]}\t{week[2]}\t{week[3]}\t{week[4]}\t{week[5]}\t{week[6]}")

print("-" *27)


