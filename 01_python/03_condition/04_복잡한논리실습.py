"""
올해 국가 지정 건강검진 대상자 기준은 다음과 같습니다.

짝수년도 출생
30세 이상

사용자에게 출생년도 4자리를 입력받아 대상자라면 True, 아니라면 False를 출력해보세요.
"""

birth_year = 1988
even = birth_year % 2 == 0
print("짝수년생인가요?", even)

this_year = 2026
age = this_year - birth_year +1
over30 = age>=30
print("30세이상인가요?", over30)

# recipient = even == True and over30 == True
recipient = even and over30
print("건강검진 대상자 : ", recipient)