"""
함수실습

다음 작업을 수행하는 함수를 만드세요.

분식집에서 사용할 수 있는 함수 생성
show_menu 함수를 만들어서 메뉴판을 출력
show_price 함수를 만들어서 떡볶이, 튀김, 순대 개수에 따른 계산 금액 출력

show_menu 함수의 예상 결과
###################
# KH 분식집
###################
# 떡볶이 3,000원
# 튀김   2,000원
# 순대   3,500원
###################


show_price 함수의 예상 결과
(단, 주문하지 않은 상품의 정보는 나오지 않도록 처리하세요)

<영수증>
-------------------
떡볶이 2인분 - 6000원
튀김 2인분 - 4000원
순대 1인분 - 3500원
--------------------
총 13500원
"""

def show_menu():
    print("#" * 20)
    print("# KH 분식점")
    print("#" * 20)
    print("# 떡볶이   3,000원")
    print("# 튀김     2,000원")
    print("# 순대     3,500원")
    print("#" * 20)

show_menu()

print("-"*30)
print()

# def show_price(dduck, fried, sundae):  # 기본값 미지정
# def show_price(rice=0, fried=0, sundae=0):  # 기본값 지정 (일부 항목이 누락될 수 있음)
def show_price(dduck=0, fried=0, sundae=0):  # 기본값 지정
    # 이 함수에서만 사용할 변수를 얼마든지 만들 수 있다.
    # 지역 변수(local variable)
    dduck_toal = dduck * 3000
    fried_total = fried * 2000
    sundae_toal = sundae * 3500
    total = dduck_toal + fried_total + sundae_toal
    print("<영수증>")
    print("-" * 20)
    if dduck > 0:
        print(f"떡볶이 : {dduck}인분 - {dduck_toal}원")
    if fried > 0:
        print(f"튀김 : {fried}인분 - {fried_total}원")
    if sundae > 0:
        print(f"순대 : {sundae}인분 - {sundae_toal}원")
    print("-" * 20)
    print(f"총합 : {total}원")

show_price(2,1,1)
print()
show_price(dduck=1)
show_price(fried=1,sundae=2)