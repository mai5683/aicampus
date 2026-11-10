"""
# 반복 카운트 실습 (05_연령대카운트.py)

고객 10명의 출생년도를 입력받아 연령대별로 카운트하는 프로그램을 만드세요
- 연령대는 10대 이하, 20대, 30대, 40대 이상 이렇게 네 가지로 구분합니다.
- 음수나 `0` 등 현재 상태에 어울리지 않는 값은 입력되지 않는다고 가정하고 따로 처리하지 않습니다.
"""

count10 = 0
count20 = 0
count30 = 0
count40 = 0

for i in range(10): #10회
    birth = int(input("출생년도(YYYY) : "))
    age = 2026 - birth + 1
    # print(f"나이는 {age}세 입니다")

    # 10대 이하, 20대, 30대, 40대를 구분하여 출력
    if age <= 19:
        count10 += 1
    elif age <= 29:
        count20 += 1
    elif age <= 39:
        count30 += 1
    else:
        count40 += 1

print(f"10대 이하 - {count10}명")
print(f"20대 - {count20}명")
print(f"30대 - {count30}명")
print(f"40대 이상 - {count40}명")