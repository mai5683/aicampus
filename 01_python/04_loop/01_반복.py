"""
반복(loop)

동일하거나 패턴이 예측 가능한 코드를 지속적으로 실행하는것
"""

# (ex) Hello Python을 10번 출력하세요
print("Hello Python")
print("Hello Python")
print("Hello Python")
print("Hello Python")
print("Hello Python")
print("Hello Python")
print("Hello Python")
print("Hello Python")
print("Hello Python")
print("Hello Python")

print()

print("Hello Python\n" * 10)

print()

# 반복구문 (x10)
# - range는 범위를 만들어내는 명령
# - range(10)은 10번(0~9)를 만들어냄 [0,1,2,3,4,5,6,7,8,9]
# - range(1,10)은 1부터 10 전까지의 범위를 만들어냄
# - i는 자동으로 증가하는 변수 (1씩 증가한다는 의미가 아님)
# - for 구문 내에서 i라는 이름의 변수를 사용할 수 있음 (이름 변경 가능)
# for i in range(5):
# for i in (10, 20, 30, 40, 50):
# x = 10
# for i in range(x):
for i in ("안","녕","하","세","요"):
    print("Hello Python", i)

