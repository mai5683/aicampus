"""
실습 문제 : 경품 당첨 프로그램
참가자의 이름을 리스트에 입력받은 뒤 1, 2, 3등 당첨인원 수를 설정하면 각각의 등수에 대한 당첨인원이 화면에 출력되도록 구현하는 프로그램을 만들고 싶습니다.

총 인원수 입력 : 6
이름 입력 : 민수
이름 입력 : 지수
이름 입력 : 지혜
이름 입력 : 철수
이름 입력 : 지후
이름 입력 : 연아

1등 수 입력 : 1
2등 수 입력 : 1
3등 수 입력 : 2

<당첨 결과>
1등 : [지후]
2등 : [지혜]
3등 : [연아, 철수]
미당첨 : [민수, 지수]


HINT

배열에서 항목을 랜덤으로 추첨하는 명령은 두 가지가 있습니다.
random.choice()
random.choices()
"""

import random

names = []

total = int(input("총 인원수 입력 : "))

for i in range(total) :
    name = input("이름 입력 : ")
    names.append(name)
print()

first = int(input("1등 수 입력 : "))
second = int(input("2등 수 입력 : "))
third = int(input("3등 수 입력 : "))
print()

first_name = []
second_name = []
third_name = []

for i in range(first) :
    winner1 = random.choice(names)
    first_name.append(winner1)

for i in range(second) :
    winner2 = random.choice(names)
    second_name.append(winner2)

for i in range(third) :
    winner3 = random.choice(names)
    third_name.append(winner3)

remaining_names = []

for i in range(total) :
    remaining_names.append(names[i])

print("<당첨 결과>")
print(f"1등 : {first_name}")
print(f"2등 : {second_name}")
print(f"3등 : {third_name}")
