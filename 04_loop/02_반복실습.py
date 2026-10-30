"""
# 반복 기본 실습 (02_반복실습.py)

다음 요구사항에 맞는 반복을 출력하세요

1. AI Campus를 5번 출력
2. `1`부터 `100`까지 정수를 출력
3. `1`부터 `100`까지 중에서 짝수만 출력
4. `1`부터 `100`까지 중에서 7로 끝나는 숫자만 출력
"""

# 1
for i in range(5):
    print("AI Campus")

print()

# 2
for i in range(1,101):
    print("1부터 100까지의 정수 :", i)

print()

# 3
# - 첫 번째 구문은 다소 느리지만 확장성이 좋다
# - 두 번째 구문은 최적의 속도를 가지지만 다른 상황에 적용이 어려움
for i in range(1,101): # 1부터 101전까지 1씩 증가
    if i % 2 == 0:
        print("1부터 100까지의 짝수 :", i)

print()

for i in range(2, 101, 2): #2부터 101전까지 2씩 증가
    print("1부터 100까지의 짝수 :", i)

print()

# 4
# - 7, 17, 27, 37, 47, 57, 67, 77, 87, 97
for i in range(1, 101):
    if i % 10 == 7:
        print("7로 끝나는 숫자 :", i)

print()

for i in range(7, 101, 10):
    print("7로 끝나는 숫자 :", i)

print()

# 추가 문제
# 1~100 사이에서 3가 들어있는 숫자만 출력
# for i in range(1, 101):
#     if i % 10 == 3 or i // 10 == 3:
#         print("3가 들어간 숫자 :", i)
print()

find = 5
for i in range(1, 101):
    ten = i // 10 == find
    one = i % 10 == find
    if ten or one:
        print(find, "가 들어간 숫자 :", i)
