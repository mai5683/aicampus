"""
# 실습 문제 : 회원가입 및 로그인 프로그램

사용자에게 다음과 같은 메뉴를 보여주고 처리하는 프로그램을 구현해주세요

```
---------------
<회원관리 v1>
---------------
1. 회원가입
2. 로그인
0. 종료
---------------
선택 :
```

- 1번을 누르면 `아이디`와 `비밀번호`를 입력받아 저장소에 등록합니다.
  - 단, 이미 등록된 아이디라면 `사용중인 아이디입니다`를 화면에 출력합니다.
  - 등록이 정상적으로 완료된다면 `회원가입이 완료되었습니다.`를 화면에 출력합니다.
  - 작업을 마치면 다시 메뉴를 출력합니다.
- 2번을 누르면 `아이디`와 `비밀번호`를 입력받아 로그인 처리를 합니다.
  - 저장소에 있는 아이디와 비밀번호가 일치하면 `로그인 성공`을 출력합니다.
  - 저장소에 있는 정보와 일치하지 않으면 `로그인 정보가 일치하지 않습니다.` 를 출력합니다.
  - 로그인을 마치면 다시 메뉴를 출력합니다.
- 0번을 누르면 `프로그램을 종료합니다`를 누르고 반복을 중지합니다.

> 가능하다면 함수를 사용하는 형태로 변경하시되
> 구현을 한 뒤에 업그레이드 하는 방향으로 하시기 바랍니다
>
> (+추가) 로그인을 하면 메뉴가 다르게 나오게 해보세요
>
> --------------------------
> OOO님 로그인 중...
> --------------------------
> 1. 내 정보
> 2. 로그아웃
> 0 종료
> --------------------------
> 선택 :
"""

# 로그인 상태를 구현하려면 변수가 하나 있어야 한다
# 논리보다는 아이디를 저장하는게 좋다
# True / False 대신에 None / 아이디 로 처리
login_user = None # 로그된 유저 아이디
database = { # 함수보다 아래 있어도 에러나지 않는다
    # "ID" : "Password"
    "testuser1" : "Testuser1!",
    "testuser2" : "Testuser2!",
    "testuser3" : "Testuser3!",
    "testuser4" : "Testuser4!"
}

def show_menu():
    if login_user is None: #비회원
        choice = menu_logout() #비회원용 메뉴를 표시
    else: #회원
        choice = menu_login() #회원용 메뉴를 표시
    return choice

def menu_login():
    print("---------------")
    print(f"<{login_user} 로그인중...>")
    print("---------------")
    print("1. 내정보")
    print("2. 로그아웃")
    print("0. 종료")
    print("---------------")
    choice = int(input("선택 : "))
    return choice

def menu_logout():
    print("---------------")
    print("<회원관리 v1>")
    print("---------------")
    print("1. 회원가입")
    print("2. 로그인")
    print("0. 종료")
    print("---------------")
    choice = int(input("선택 : "))
    return choice

def member_join():
    id = input("아이디 입력 : ")
    pw = input("비밀번호 입력 : ")

    if id in database:
        print("이미 사용중인 아이디입니다")
    else:
        database[id] = pw  # 실제 등록 코드
        print("회원가입이 완료되었습니다")

def member_login():
    id = input("아이디 입력 : ")
    pw = input("비밀번호 입력 : ")
    is_login = id in database and database[id] == pw  # 올바른 코드

    if is_login:
        global login_user #이건 밖에 있는거에요(비추)
        login_user = id
        print("로그인 성공")
    else:
        print("로그인 정보가 일치하지 않습니다")

def power_off():
    print("프로그램을 종료합니다")
    exit(0)

# main()
while True:
    choice = show_menu()
    if choice == 1: # 회원가입
        member_join()
    elif choice == 2: # 로그인
        member_login()
    elif choice == 0:
        power_off()

