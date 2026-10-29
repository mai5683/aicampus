"""
실습문제 : 계절 판정하기

사용자에게 월을 입력받아 계절을 출력하세요.
(단, 사용자는 무조건 1~12를 입력한다고 가정합니다)

봄 : 3, 4, 5월
여름 : 6, 7, 8월
가을 : 9, 10, 11월
겨울 : 12, 1, 2월
"""

# 입력
# 출력
# if 3 <= month <= 5 :  # 3~5월
# if month >= 3 and month <= 5 :  # 3월 이상 5월 이하
# if month > 2 and month < 6 :  # 2월 초과 6월 미만
# if month in (3, 4, 5) :  # 3, 4, 5 중 하나
#

month = int(input("월 : "))

if month >= 3 and month <= 5 :
    print("봄")
elif month >= 6 and month <= 8 :
    print("여름")
elif month >= 9 and month <= 11 :
    print("가을")
else :
    print("겨울")

#  내가 작성한 답안
# if month == 3 or month == 4 or month == 5 :
#    print("봄")
# elif month == 6 or month == 7 or month == 8 :
#     print("여름")
# elif month == 9 or month == 10 or month == 11 :
#     print("가을")
# elif month == 12 or month == 1 or month == 2 :
#     print("겨울")
