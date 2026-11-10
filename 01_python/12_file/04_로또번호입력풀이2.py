"""
파일 입출력 실습 : 로또번호 저장하고 불러오기
파일명 : 03_로또번호출력.py , 04_로또번호입력.py

03번 프로그램에서 로또번호를 6개 생성하여 프로그램과 같은 위치에 lotto.txt라는 이름으로 저장합니다
04번 프로그램에서 저장된 내용을 읽어 화면에 출력하도록 구현합니다
"""


print("저장된 로또번호를 읽고 있습니다")
file = open("lotto1.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()
print("저장된 로또번호 읽기가 완료되었습니다")

lotto1 = []
for line in lines:
    number = int(line.strip())
    lotto1.append(number)

print("<로또 번호>")
for line in lines:
    print(line.strip())
