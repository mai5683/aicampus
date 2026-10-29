# 문제2. 거스름돈 계산

bread_price = 3500
bread_count = 2
cake_price = 4200
cake_count = 1
amount_paid = 20000

bread_total = bread_price * bread_count
cake_total = cake_price * cake_count
total = bread_total + cake_total
change = amount_paid - total

print("총금액 :", total, "원")
print("거스름돈 :", change, "원")