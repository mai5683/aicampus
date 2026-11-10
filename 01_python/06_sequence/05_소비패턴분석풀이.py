"""
일주일 동안 사용한 용돈을 입력해서 분석하는 프로그램을 구현하려고 합니다.

1. 먼저 총 용돈을 입력합니다.
2. 그리고 요일별(월,화,수,목,금,토,일)로 일주일간 사용한 용돈을 입력합니다
3. 잔액을 출력해보세요
4. 하루 평균보다 많이 사용한 날의 금액만 출력해보세요
5. 전체 용돈 사용내역을 출력하면서 4번에 해당하는 금액 옆에 (과소비)를 붙여서 출력하세요
6. 월요일에 사용한 용돈은 이번주 중 몇 번째로 많은 금액인지 계산해서 출력하세요
"""

# 1.
pocket_money = int(input("총 용돈 입력 : "))

# 2.
daily = []

for i in range(7) :
    money = int(input("일 금액 입력 : "))
    daily.append(money)

# 3. 잔액을 출력하려면 daily의 합계가 필요
daily_total = 0
for money in daily:
    daily_total += money
# print(daily_total)
# print(sum(daily))  # list의 합계를 구해주는 명령
balance = pocket_money - daily_total  # sum(daily) 로도 가능
print("잔액 :", balance, "원")

# 4. 평균 = 합계 / 개수, 개수는 지금 7개이지만 len( ) 사용 권장
daily_average = daily_total / len(daily)
print("일 평균 :", daily_average, "원")

# 평균 이상인 금액만 출력
print("<평균보다 초과 지출한 경우>")
for money in daily :
    if money > daily_average :
        print("금액 :", money, "원")

# 5.
print("<전체 지출 내역>")
for money in daily :
    if money > daily_average :
        print("금액 :", money, "원 (과소비)")
    else :
        print("금액 :", money, "원")

# 6.
rank = 1                          # 최초 랭크를 1로 가정
# target = daily[0]               # 비교할 점수를 보관
for money in daily :              # 모든 금액을 비교하며
    if money > daily[0] :         # 더 큰 금액을 발견하면
        rank += 1                 # 등수를 1 증가 (뒤로 밀어내기)

print(int(f"월요일에 사용한 금액은 이번 주 중에서 {rank}등으로 많습니다."))