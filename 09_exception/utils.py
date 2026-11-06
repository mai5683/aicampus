# utils.py에 함수를 만들어 두고 불러 와서 사용
from utils import seperate_data
from utils import calculate_korean_age
from utils import calculate_global_age

# main
try:  # 플랜 A
    birth = input("생년월일(YYYY-MM-DD) 입력 : ")
    year, month, day = seperate_date(birth)
    korean_age = calculate_korean_age(year)
    global_age = calculate_global_age(year, month, day)

    print(f"한국나이 : {korean_age}세")
    print(f"만나이 : {global_age}세")
except Exception as e:  # 플랜 B
    # print("프로그램상의 오류가 발생했습니다")
    print(f"오류 : {e}")
