""""
# 문구점에서 다음 물건을 구매했습니다.

공책: 2000원짜리 3권
연필: 800원짜리 2자루
지불한 금액: 10000원

각 물건의 총가격을 계산하세요.
총 구매 금액을 계산하세요.
거스름돈을 계산하세요.
총 구매 금액과 거스름돈을 각각 출력하세요.
"""

# 물건 가격과 개수
notebook_price = 2000
notebook_count = 3
pencil_price = 800
pencil_count = 2

# 지불한 금액
amount_paid = 10000

# 각 물건의 총가격 계산
notebook_total = notebook_price * notebook_count
pencil_total = pencil_price * pencil_count

# 총 구매 금액 계산
total = notebook_total + pencil_total

# 거스름돈 계산
change = amount_paid - total

# 결과 출력
print(total)
print(change)
