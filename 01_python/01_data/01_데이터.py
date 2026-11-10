"""
데이터(data) : 측정이 가능한 값 (바나나 한개의 가격)
정보(information) : 데이터로 만들어낸 계산결과 (바나나 가격 동향, 평균)
연산(operation) : 데이터로 정보를 만들어내는 과정 (더하기, 빼기 등)

프로그래밍은 데이터를 이용해서 정보를 만들어내 판단을 하는 것

가장 중요한 데이터는 숫자이고, 글자, 논리 등 다양한 형태가 존재
"""


# (ex) 피자가 한판에 2만원일 때, 3판을 주문하면 얼마일까요?
print("60000원") # 내가 계산한 결과
print("20000*3") # 글자로 처리됨
print(20000*3, "원") # 연산한 결과가 출력

# (ex) 자장면 8천원, 짬뽕 12천원일 때 자장면 3그릇과 짬뽕 2그릇의 가격은?
print(8000*3+12000*2, "원") # 우리는 이미 곱하기가 먼저 계산된다는 걸 압니다 (사전지식)

# (ex) 치킨이 2만원, 치킨무가 700원, 감자튀김이 3500원일 때 치킨2+치킨무2+감자튀김1 가격은?
print(20000*2+700*2+3500*1, "원")

# 문제점 : 어느 값이 무슨 항목인지 알기가 어렵다 (가독성이 떨어진다. 유지, 보수가 어렵다.)
# 변수(variable)를 사용해서 값을 저장해두고 사용
a = 20000*2
b = 700*2
c = 3500*1
print(a+b+c)

# 문제점 : 가격과 수량이 구분이 안 된다.
chicken_price = 20000
chicken_count = 2
radish_pirce = 700
radish_count = 2
fries_price = 3500
fries_count = 1

chicken_total = chicken_price * chicken_count
radish_total = radish_pirce * radish_count
fries_total = fries_price * fries_count

total = chicken_total + radish_total + fries_total
print(total)