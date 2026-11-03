"""
calc_time 함수를 만들어서 전달받은 시작시간과 종료시간의 차이를 계산해 출력해보세요

calc_time 함수의 예상 결과

시작 시각 : 2시 50분
종료 시각 : 4시 30분
-------------------
이용 시간 : 1시간 40분


이 함수를 구현하기 위해 필요한 값들을 함수에 변수로 선언한 뒤 처리해보세요
"""

def calc_time(
        in_hour, in_minute,
        out_hour, out_minute
):
    in_time = in_hour * 60 + in_minute
    out_time = out_hour * 60 + out_minute
    time = out_time - in_time
    hour = time // 60
    minute = time % 60
    print(f"시작 시각 : {in_hour}시간 {in_minute}분")
    print(f"시작 시각 : {out_hour}시간 {out_minute}분")
    print("-"*20)
    print(f"시작 시각 : {hour}시간 {minute}분")

calc_time(1, 2,
          4, 30
)
