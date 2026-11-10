"""
# 파일 입출력 실습 : 로또번호 저장하고 불러오기

파일명 : `03_로또번호출력.py` , `04_로또번호입력.py`

- 03번 프로그램에서 로또번호를 6개 생성하여 프로그램과 같은 위치에 `lotto.txt`라는 이름으로 저장합니다
- 04번 프로그램에서 저장된 내용을 읽어 화면에 출력하도록 구현합니다
"""

print("저장된 로또번호를 읽고 있습니다")
file = open("lotto2.txt", "r", encoding="utf-8")
line = file.readline().strip() # 한 줄에 숫자가 다 있음 (콤마로 구분)
file.close()
print("저장된 로또번호 읽기가 완료되었습니다")

line = line.replace(" ", "")    #모든 공백 제거 (안쪽까지), 혹시 몰라서
lotto = line.split(",")     #콤마를 기준으로 잘라라

print("<로또 번호>")
for number in lotto:
    print(number)