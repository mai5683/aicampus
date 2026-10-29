"""
이번에는 영화관에서 간식 구매 금액 계산하기야.

팝콘은 한 개에 5,000원이고 2개를 구매했어. 음료수는 한 잔에 2,000원이고 3잔을 구매했어. 총 20,000원을 지불했어.
요구사항: 총 구매 금액과 거스름돈을 계산하고 출력하는 코드를 작성해 봐.
"""

popcorn_price = 5000
popcorn_count = 2
drink_price = 2000
drink_count = 3
amount_paid = 20000

popcorn_total = popcorn_price * popcorn_count
drink_total = drink_price * drink_count
total = popcorn_total + drink_total
change = amount_paid - total

print(total)
print(change)