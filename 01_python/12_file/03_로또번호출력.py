"""
파일 입출력 실습 : 로또번호 저장하고 불러오기
파일명 : 03_로또번호출력.py , 04_로또번호입력.py

03번 프로그램에서 로또번호를 6개 생성하여 프로그램과 같은 위치에 lotto.txt라는 이름으로 저장합니다
04번 프로그램에서 저장된 내용을 읽어 화면에 출력하도록 구현합니다
"""

import random

file = open("lotto.txt", "w", encoding="utf-8")

# 로또 번호가 담긴 통 생성
numbers = list[int](range(1,46))
lotto = []

random.shuffle(numbers)
lotto = numbers[:6]

file.write(str(lotto))
file.close()
