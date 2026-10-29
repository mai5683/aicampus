"""
논리(bool)

판정을 내리기 위한 값
값은 True, False 두 개 뿐이다.

숫자를 비교연산하여 만들어낼 수 있다.
비교연산자 : 크다(<), 작다(<), 이상(<=), 이하(<=), 같다(==), 다르다(!=)
"""

a = True
b = False
print(a, b)

# (ex) 피자를 주문할 수 있나요? 피자 주문가능 판단
money = 30000
pizza = 30000
# order = money가 pizza보다 많아요? # 비교
order = money >= pizza
print(order)
