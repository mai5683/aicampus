"""
실습 과제
파일명 : 02_나이구하기.py

사용자에게 YYYY-MM-DD 형태의 날짜를 입력 받아 다음을 구하세요.

- 한국 나이 (korean_age)
- 만 나이 (global_age)

한국나이는 연도만으로 계산하며, 만 나이는 연월일 다 필요하지만 계산 편의상 연도와 월 정보만 추출해서 계산하도록 변경하겠습니다. 만 나이는 12개월당 한 살인걸로 간주합니다.

프로그램에서 발생하는 예외 상황들이 모두 처리될 수 있도록 코드를 구현하세요.
"""

# 플랜A를 먼저 구성

birth = "2005-05-02"

year = int(birth[:4])
month = int(birth[5:7])
day = int(birth[8:])
# print(year, month, day)

korean_age = 2026 - year + 1  # 한국나이

# 현재 문제에서의 만나이(현재날짜(월) - 태어난날짜(월) // 12)
# 실제 만나이 : 생일이 지나면
today = 2026 * 12 + 11  # 2026년 11월
born = year * 12 + month
diff = today - born
# print("diff", diff)
global_age = diff // 12


print(f"한국나이 : {korean_age}세")
print(f"만나이 : {global_age}세 ({diff}개월)")