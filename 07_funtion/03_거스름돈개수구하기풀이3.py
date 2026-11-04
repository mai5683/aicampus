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
from itertools import count


# receipt  함수를 만들어서 호출하면 영수증이 나오도록 변경
def receipt(price, pay) :
    # 연산
    change = pay - price
    copy = change  # change가 변하지 않게 하기 위해 복사

    # 변경 : 어차피 50000 → 10000 → 5000 → 1000 → 500 → 100 → 50 → 10 순서일 테니...
    money = [50000,10000,5000,1000,500,100,50,10]
    counts = []

    for m in money :
        counts.append(copy // m)
        copy %= m

    counts.append(copy // money[0])
    copy %= money[0]
    counts.append(copy // money[1])
    copy %= money[1]
    counts.append(copy // money[2])
    copy %= money[2]
    counts.append(copy // money[3])
    copy %= money[3]
    counts.append(copy // money[4])
    copy %= money[4]
    counts.append(copy // money[5])
    copy %= money[5]
    counts.append(copy // money[6])
    copy %= money[6]
    counts.append(copy // money[7])
    copy %= money[7]

    print("<영수증>")
    print(f"상품 가격 : {price}원")
    print(f"지불 금액 : {pay}원")
    print("-" * 20)
    print(f"거스름돈 : {change}원")

    for i in range(len(money)):
        if counts[i] > 0 :
            print(f"  +-- {money[i]}원짜리 {counts[i]}개")
        print("-"*20)

# -------------------------------------
# main 프로그램
# -------------------------------------
receipt(5750, 6000)