"""
csv/monsters.csv를 읽는 예제

출력할 때와 동일하게 중첩 리스트 형태로 읽어봅니다.

*(주의) 불러온 모든 데이터는 문자열입니다.
"""

import csv

monsters = []
with open("csv/monsters.csv", "r",
            encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file)   # csv 입력 도구 생성
    for row in reader:
        monsters.append(row)

print(monsters)
