"""
리스트에 데이터를 미리 넣어두는 게 아니라 원할 때 추가
"""

# 비어 있는 리스트를 준비
scores =[]

# 데이터 추가 (append - 맨 뒤에 데이터를 추가)
for i in range(5) :  # 다섯 번 / ( ) 안에 입력할 횟수
    number = int(input("숫자 입력 : "))
    scores.append(number)

print(scores)
#               ----------> 이렇게 하면 출력 시 [10, 20, 30, 40, 50] 으로 나옴

# list의 길이를 확인
print(len(scores))