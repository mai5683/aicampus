"""
네이버에서 "사다리게임"을 검색해서 나온 프로그램을 텍스트 버전으로 만드세요
"""
# 참여 인원수, 이름, 당첨항목 입력 받기


import random

persons = int(input("참여 인원수 : "))
if persons <= 1 :
    print("참여 인원은 2명 이상이어야 합니다.")
else :
    names = []
    items = []

    for i in range(persons) :
        name = input("참여자 이름 : ")
        names.append(name)

    for i in range(persons):
        item = input("당첨 항목 : ")
        items.append(item)

    # 셔플
    random.shuffle(items)

    for i in range(persons):
        print(f"{names[i]} → {items[i]}")

