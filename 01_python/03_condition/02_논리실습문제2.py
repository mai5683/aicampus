"""
PC방에서 고객의 이용시간에 따라 요금을 계산하는 프로그램을 만들고 있습니다.
1시간에 1,000원의 요금을 받고 있는데, 급한 출력 등으로 1시간 미만으로 이용하는 고객이 늘어나서 기본요금 제도를 도입하기로 했습니다.

고객의 시작, 종료시간과 분을 각각 입력받아서 1시간 미만으로 이용한 경우 True, 1시간 이상 이용한 경우 False로 판정하는 기본요금 판정기를 구현해보세요
"""

in_hour = int(input("시작시각(시간) : "))
in_minute = int(input("시작시각(분) : "))
out_hour = int(input("종료시각(시) : "))
out_minute = int(input("종료시각(분) : "))

in_time = in_hour * 60 + in_minute
out_time = out_hour * 60 + out_minute
time = out_time-in_time

hour = time//60
minute = time%60

basic_rate = time < 60

print("이용시간 : ", hour, "시간", minute, "분")
print("기본요금 대상 : ", basic_rate)
