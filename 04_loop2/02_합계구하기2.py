"""
While 실습문제

사용자가 입력한 숫자들을 계속 더해서 종료 시 합계와 평균을 출력하는 프로그램을 구현하세요
단, 사용자가 0을 입력하면 종료되며 0은 입력으로 간주하지 않습니다

숫자 입력 : (10)
숫자 입력 : (20)
숫자 입력 : (30)
숫자 입력 : (0)

합계 : 60
평균 : 20
"""

# total = 총합, count = 입력된 user마다 추가
total = 0
count = 0

while True :
    user = int(input("숫자 입력 : "))

    # (추가) 음수는 처음부터 다시 시작
    if user < 0 :
        continue

    # 0인 경우는 제외하고 카운트와 합계 계산
    if user == 0 :
        break

    # else가 없어도 else처럼 사용된다 (break 때문에)
    total += user
    count += 1

average = total / count

print(f"합계 : {total}")
print(f"평균 : {average}")