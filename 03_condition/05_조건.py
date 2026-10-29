"""
조건(condition)

특정 상황을 만족해야 실행되는 형태의 구도

if 판정식 :
    Ture일 때 실행될 코드  → 아래 출력코드는 Tab키 누른 후 입력

아닌 경우도 처리하고 싶다면 if 뒤에 else 추가

fi 판정식 :
    True일 때 실행될 코드
else :
    False일 떄 실행될 코드
"""

age = 10

if age >= 20 :
    print("성인입니다")
    print("입장 가능합니다")

# if age < 20 :
else :
    print("미성년자입니다")
    print("입장 불가능합니다")