"""
딕셔너리 데이터도 CSV로 내보낼 수 있다.
"""

import csv

monsters = [
    {"no" : 4, "name" : "파이리", "type" : "불꽃"},
    {"no" : 7, "name" : "꼬부기", "type" : "물"},
    {"no" : 25, "name" : "피카츄", "type" : "전기"},
]

with open("csv/monsters.csv", "w",
          encoding="utf-8-sig", newline="") as file:
    # writer = csv.writer(file)   # 기존 방법
    writer = csv.DictWriter(
        file,   # 저장 대상 파일
        # fieldnames = ["no", "name", "type"]
        fieldnames = monsters[0].keys()
    )

    writer.writeheader()    # 헤더(제목) 먼저 기록
    writer.writerows(monsters)

print("csv 저장 완료")

