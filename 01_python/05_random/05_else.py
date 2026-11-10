"""
반복문에도 else를 쓸 수 있다.

else는 반복이 정상적으로 종료된 이후 실행
(지정된 횟수를 다 채운 경우)
"""

# (ex) 숫자 10번 입력 받기 (단, 0 입력 시 종료)

for i in range(10) :
    number = int(input("숫자 입력 : "))

    if number == 0 :
        break

else :
    print("정상 종료되었습니다.")