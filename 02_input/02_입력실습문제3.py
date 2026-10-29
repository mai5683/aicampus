"""
할인가격 계산하기

상품의 원래 가격과 할인율을 입력 받아 할인금액과 최종가격
(단, 금액은 소수점이 나올 수 없습니다)
계산식 : 할인금액 = 원래가격 x 할인율 / 100
"""

# 입력
price = int(input("금액입력 : "))
rate = float(input("할인율입력 : "))

# 연산
# discount = price*rate//100
discount = int(price*rate/100)
# result = price*(100-rate)//100 #비추천
result = price - discount # 추천

# 출력
print("할인금액 : ", discount)
print("최종가격 : ", result)
