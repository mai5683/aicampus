"""
함수 실습 : 잔액과 거스름돈 개수 구하기
상품 금액과 지불한 금액을 이용해서 다음과 같은 영수증을 출력하는 함수를 만드세요

<구매 영수증>
-------------------
상품 가격 : 55750원
지불 금액 : 60000원
-------------------
거스름돈 : 4250원
 +-- 1000원짜리 4장
 +-- 100원짜리 2개
 +-- 50원짜리 1개


5만원짜리부터 개수를 검사하며, 줄 필요 없는 금액에 대해서는 출력하지 않습니다.
"""


def receipt(price, pay):
    change = pay-price

    print("<구매 영수증>")
    print("-" * 20)
    print(f"상품 가격 : {price}원")
    print(f"지불 금액 : {pay}원")
    print("-" * 20)
    if change > 0:
        print(f"거스름돈 : {change}원")

    fifty_thousand_won = change // 50000
    change = change % 50000
    ten_thousand_won = change // 10000
    change = change % 10000
    five_thousand_won = change // 5000
    change = change % 5000
    one_thousand_won = change // 1000
    change = change % 1000
    five_hundred_won = change // 500
    change = change % 500
    one_hundred_won = change // 100
    change = change % 100
    fifty_won = change // 50
    change = change % 50
    ten_won = change // 10
    change = change % 10

    if fifty_thousand_won > 0 :
        print(f" +-- 50000원짜리 {fifty_thousand_won}장")
    if ten_thousand_won > 0 :
        print(f" +-- 10000원짜리 {ten_thousand_won}장")
    if five_thousand_won > 0 :
        print(f" +-- 5000원짜리 {five_thousand_won}장")
    if one_thousand_won > 0 :
        print(f" +-- 1000원짜리 {one_thousand_won}장")
    if five_hundred_won > 0:
        print(f" +-- 500원짜리 {five_hundred_won}장")
    if one_hundred_won > 0 :
        print(f" +-- 100원짜리 {one_hundred_won}개")
    if fifty_won > 0 :
        print(f" +-- 50원짜리 {fifty_won}개")
    if ten_won > 0 :
        print(f" +-- 10원짜리 {ten_won}개")

receipt(5650, 10000)

