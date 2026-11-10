"""
일주일 동안 사용한 용돈을 입력해서 분석하는 프로그램을 구현하려고 합니다.

1. 먼저 총 용돈을 입력합니다.
2. 그리고 요일별(월,화,수,목,금,토,일)로 일주일간 사용한 용돈을 입력합니다
3. 잔액을 출력해보세요
4. 하루 평균보다 많이 사용한 날의 금액만 출력해보세요
5. 전체 용돈 사용내역을 출력하면서 4번에 해당하는 금액 옆에 (과소비)를 붙여서 출력하세요
6. 월요일에 사용한 용돈은 이번주 중 몇 번째로 많은 금액인지 계산해서 출력하세요
"""

pocket_money = int(input("총 용돈 : "))
day_of_the_week = ["월","화","수","목","금","토","일"]
total = 0
use_money = []

for i in range(7) :
    use = int(input(f"{day_of_the_week[i]}요일 사용한 용돈 : "))
    use_money.append(use)
    total += use
balance = pocket_money - total
print(f"잔액 : {balance}원")


average = total / 7
for i in use_money :
    if average < use_money[i] :
        print(f"과소비 : {day_of_the_week[i]}요일, {use_money[i]}원")
