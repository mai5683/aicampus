"""
함수(Funtion)

기존에 만든 코드들 중
반복적으로 다시 사용할 가치가 있는 코드들에
이름을 붙여 보관하는 도구
"""

# test라는 이름의 함수
# 코드만 가지고 있다가 별도의 실행코드를 만나야 실행 가능하다.
def test() :
    print("테스트 코드")

# test라는 함수를 실행(호출)
test()
test()
test()

# add라는 이름의 함수
# - 숫자 두 개만 전달하면 알아서 더해서 출력까지 해주는 함수
# - 함수에도 숫자 두 개를 저장할 변수가 있어야 한다.
def add(left, right) :
    result = left + right
    print(f"{left} 더하기 {right}는 {result}입니다.")

add(1, 2)  # add라는 함수에 1, 2를 전달하며 실행시키겠다.
add(10, 20)  # add라는 함수에 10, 20을 전달하며 실행시키겠다.
add(left=100, right=200)


