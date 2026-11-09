"""
CSV 출력 예제

사용을 위해서 csv 모듈을 불러와야 합니다.

import csv

1. 중첩 리스트 형태
2. Dictionary 형태

위 두 가지를 csv로 내보낼 수 있습니다.
"""

import csv
from pathlib import Path

monsters = [
    ["no", "name", "type"],    # 1줄(제목)
    [4, "파이리", "불꽃"],       # 1줄(데이터)
    [7, "꼬부기", "물"],         # 1줄(데이터)
    [25, "피카츄", "전기"]       # 1줄(데이터)
]

# 디렉터리 생성
dir = Path("csv")
dir.mkdir(exist_ok=True)

# csv 저장 (파일과 동일하게 open으로 시작)
with open("csv/monsters.csv", "w",
          encoding="utf-8-sig", newline="") as file:
                         # csv 할 때만 -sig 추가
    writer = csv.writer(file)   # csv 저장도구 생성
    writer.writerows(monsters)   # 모든 줄을 저장하도록 지시
    # writer.writerow(monsters[0])
    # writer.writerow(monsters[1])
    # writer.writerow(monsters[2])

print("csv 데이터 저장 완료")