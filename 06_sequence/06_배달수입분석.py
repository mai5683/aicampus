"""
# 과제 : 배달기사 수입 정산

배달기사가 하루 동안 총 8건의 배달을 완료했습니다.
각 배달의 수입은 배달 거리와 관계없이 주문마다 다르게 지급됩니다.

8건의 배달 수입을 차례대로 입력받아 리스트에 저장하고, 반복문과 조건문을 사용하여 다음 기능을 구현하세요.

요구사항
- 하루 동안 벌어들인 총 배달 수입을 계산하여 출력하세요.
- 배달 1건당 평균 수입을 계산하여 출력하세요.
- 평균 수입보다 높은 배달 건의 수입만 출력하세요.
- 배달 수입이 5,000원 이상인 건수를 구하여 출력하세요.
- 배달 수입이 가장 높은 건과 가장 낮은 건의 금액 차이를 계산하세요.
- 배달기사는 하루 수입의 10%를 오토바이 유지비로 사용합니다. 유지비를 제외한 실제 수입을 계산하세요.
- 하루 목표 수입이 50,000원이라면 목표까지 얼마나 부족한지 또는 얼마나 초과했는지 출력하세요.

명령 찾아서 사용하는 것과 직접 계산하여 구하는 것의 차이를 확인해보세요
"""

delivery = []

for i in range(8) :
    income = int(input("배달 수입 : "))
    delivery.append(income)
total = sum(delivery)
print("총 배달 수입 :", total)

number = len(delivery)
average = total // number
print("배달 1건당 평균 수입 :", average)

count = 0
print("<평균 수입보다 높은 배달건의 수입>")
for income in delivery :
    if income > average :
        print(income)

    if income >= 5000 :
        count += 1
print("배달 수입이 5000원 이상인 건수 :", count)

maximum = delivery[0]
minimum = delivery[0]
for income in delivery :
    if income > maximum :
        maximum = income
    if income < minimum :
        minimum = income
difference = maximum - minimum
print("최대 수입과 최저 수입의 차액 :", difference)

cost = total * 10 // 100
actual_earnings = total - cost
print("유지비 제외한 실제수입 :", actual_earnings)

target = 50000 - actual_earnings
if actual_earnings < 50000 :
    print("목표까지 부족한 금액 :", target)
elif actual_earnings > 50000 :
    print("목표보다 초과한 금액 :", target)
else :
    print("목표금액과 동일")

