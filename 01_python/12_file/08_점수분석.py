"""
CSV 실습
다음 데이터를 파일을 만들어 저장하고 불러와서 출력해보세요

08_점수등록.py에서는 csv/scores.csv에 제시된 점수를 등록하는 코드를 작성하세요
08_점수분석.py에서는 csv/scores.csv에 제시된 점수를 읽어들여 다음을 구하세요
총 평균

이름은 name, 국어는 kor, 영어는 eng, 수학은 mat라는 이름을 사용하세요
"""

import csv

total = 0
count = 0

with open("csv/scores.csv", "r",
          encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file)   # csv 입력 도구 생성
    for row in reader:      # 한 줄씩
        for data in row:    # 한 칸씩
            try:
                # print(int(data))
                total += int(data)
                count += 1
            except Exception:
                pass

print("합계", total)
print("개수", count)
print("평균", total/count)