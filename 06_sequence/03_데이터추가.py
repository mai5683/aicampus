"""
리스트에 데이터를 미리 넣어두는 게 아니라 원할 때 추가
"""

# 비어 있는 리스트를 준비
scores =[]

# 데이터 추가 (append - 맨 뒤에 데이터를 추가)
# scores[0] = 10  # +0 지점에 10을 넣으세요. (수정할 떄만 가능)
scores.append(10)
scores.append(20)
scores.append(30)
scores.append(40)
scores.append(50)

print(scores)
#               ----------> 이렇게 하면 출력 시 [10, 20, 30, 40, 50] 으로 나옴

# list의 길이를 확인
print(len(scores))