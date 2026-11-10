"""
파일 입출력 실습 : 로또번호 저장하고 불러오기
파일명 : 03_로또번호출력.py , 04_로또번호입력.py

03번 프로그램에서 로또번호를 6개 생성하여 프로그램과 같은 위치에 lotto.txt라는 이름으로 저장합니다
04번 프로그램에서 저장된 내용을 읽어 화면에 출력하도록 구현합니다
"""

# import random
from random import shuffle

# 로또 번호가 담긴 통 생성
print("로또 번호가 담긴 통을 생성합니다")
numbers = list(range(1, 46))
print("로또 번호를 무작위로 섞습니다")
shuffle(numbers)
print("로또 번호를 추첨합니다")
lotto1 = numbers[:6]
print("로또 번호를 순서대로 재배치합니다")
lotto1.sort()
print("추첨이 완료되었습니다")

print("추첨된 번호를 저장합니다")

file = open("lotto1.txt", "w", encoding="utf-8")
for number in lotto1:
    file.write(str(number) + "\n")
file.close()

print("추첨된 번호 저장이 완료되었습니다")
