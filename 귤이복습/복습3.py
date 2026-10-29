"""
주차장에서 1시간 미만으로 주차한 고객에게는 기본요금 2,000원을 받습니다.
주차 시작 시각과 종료 시각을 각각 시간과 분으로 입력받으세요.
총 주차시간을 분으로 계산하세요.
주차시간을 시간과 분으로 나누어 출력하세요.
주차시간이 60분 미만이면 True, 60분 이상이면 False를 출력하세요.
"""

in_hour = int(input("입차시각(시간) : "))
in_minute = int(input("입차시각(분) : "))
out_hour = int(input("출차시각(시간) : "))
out_minute = int(input("출차시각(분) : "))
in_time = in_hour * 60 + in_minute
out_time = out_hour * 60 + out_minute
time = out_time - in_time
basic_rate = time < 60
print(basic_rate)
