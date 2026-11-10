"""
<리스트 기본실습>

다음 요구사항에 맞는 프로그램을 구현하세요

──────────────────────────────────────────────────────
과일 목록 출력하기

다음과 같은 과일 목록을 리스트로 만드세요.
→ 사과, 바나나, 포도, 딸기
반복문을 사용하여 과일을 한 줄에 하나씩 출력하세요.
──────────────────────────────────────────────────────
금액 합계 구하기

중고어플에서 확인한 그래픽카드 시세는 다음과 같았습니다
→ 95만원, 92만원, 100만원, 105만원, 130만원

이 금액들을 리스트에 저장하고 출력하시고, 평균 가격을 구해서 출력해주세요
──────────────────────────────────────────────────────
"""

# 1번
fruits = ["사과", "바나나", "포도", "딸기"]

print(fruits[0], fruits[1], fruits[2], fruits[3])

# for i in range(4) :
#     print(fruits[i])

for fruit in fruits :
    print(fruit)

print("-"*30)

# 2번
graphic_cards = [950000, 920000, 1000000, 1050000, 1300000]
#                       +--------+--------+--------+---------+--------+
#                       +0      +1       +2       +3        +4        +5

# for i in range(5) :
#     print(graphic_cards[i])

# 출력만
for graphic_card in graphic_cards :
    print(graphic_card)

# 합계만
total = 0
for graphic_card in graphic_cards :
    total += graphic_card
    print(total)
average = total / 5
print(average)