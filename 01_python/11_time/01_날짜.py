"""
날짜(datetime)


"""

# datatime 모듈을 다 불러오지 않고 그 중에서 date만 골라서 불러오겠다.
# import datetime 하는 것보다 코드가 짧아짐.
from datetime import date, timedelta

# 1. 오늘 정보
# today = datetime.date.today()
today = date.today()

print(today, type(today))
print(today.year, type(today.year))
print(today.month, type(today.month))
print(today.day, type(today.day))

# 2. 원하는 날짜를 생성
birthday = date(2000, 5, 20)
print(birthday)
print(birthday.year)
print(birthday.month)
print(birthday.day)

# 3. 날짜 간 차이를 계산
diff = today - birthday
print(diff, type(diff))
print(diff.days)
print(diff.seconds)
print(diff.microseconds)

# 4. 날짜를 서로 비교하기
# - 비교연산을 그대로 사용 (이상, 이하, 초과, 미만, 같다, 다르다)
someday = date(2027, 1, 1)
print(today < someday)  # someday가 미래의 날짜인가?

# 5. 날짜 계산 (더하기, 빼기)
# - 날짜의 차이, 간격은 날짜와 다른 개념 (timedelta)
# - 계산할 때 date가 아니라 timedelta를 더하거나 뺀다.
# - weeks, days, hours, minutes, seconds 등을 쓸 수 있다.

# tomorrow = today + 1  # error
tomorrow = today + timedelta(days=1)
print(tomorrow)

yesterday = today - timedelta(days=1)
print(yesterday)

after_week = today + timedelta(weeks=1)
print(after_week)

# 6. 요일 정보 확인하기 + 출력 형식 변경하기
print(today.weekday())  # 월(0), 화(1), ..., 토(5), 일(6)
print(today.isoweekday())   # 월(1), 화(2), ..., 토(6), 일(7)

# 수동으로 요일을 보여주려면
weekdays = "월화수목금토일"
print(weekdays[today.weekday()])

# 파이썬에서 제공하는 변환 명령
# import locale
# locale.setlocale(locale.LC_TIME, "Korean_Korea.949")  # 나라별로 설정할 수 있음
print(today.strftime("%A"))   # strftime = string format time 의 줄임말
print(today.strftime("%a"))

# 각종 형식들을 활용해서 원하는 형태로 출력
# - (주의) %m은 무조건 2자리가 나옴
#    - 1자리만 나오게 하고 싶으면 (윈도우) %#m, (리눅스) %-m
#    - %d 등 대부분의 기능이 비슷함
print(today.strftime("2026년 11월 6일 오후 5시 7분 20초"))

print(today.strftime("%Y년 %#m월 %#d일 %p %#I시 %#M분 %#S초"))
print(today.strftime("%Y년 %#m월 %#d일 %#H시 %#M분 %#S초"))



