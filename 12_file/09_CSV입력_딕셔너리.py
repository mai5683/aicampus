"""
csv의 데이터를 딕셔너리 형태로 입력 받기
"""

import csv

monsters = []

with open("csv/monsters.csv", "r",
          encoding = "utf-8-sig", newline="") as file:
    # reader = csv.reader(file)   # 기존 코드
    reader = csv.DictReader(file)
    for row in reader:
        # print(row)
        # print(type(row))
        monsters.append(row)

print(monsters)