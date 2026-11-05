"""
정규표현식 종합 실습 : AI 학습 데이터 파일명 검증
파일명 : 06_정규표현식_파일명검증.py

머신러닝(ML)과 딥러닝(DL)에서는 학습용 데이터와 테스트용 데이터를 구분하고, 데이터가 생성된 날짜를 파일명에 기록하여 관리하기도 합니다.

사용자에게 파일명을 입력받아 다음 규칙에 맞는 파일명인지 검사하는 프로그램을 구현하세요.

# 파일명 형식
- 데이터구분_데이터이름_날짜.확장자

- 예시 : train_cat01_20261105.jpg

# 요구사항
1. 데이터 구분
- 반드시 train, test, valid 중 하나여야 합니다.
2. 데이터 이름
- 영문 소문자와 숫자만 사용할 수 있습니다.
- 최소 3글자, 최대 15글자입니다.
- 숫자가 반드시 1개 이상 포함되어야 합니다.
- admin이라는 단어가 포함되면 안 됩니다.
3. 날짜
- YYYYMMDD 형식의 숫자 8자리여야 합니다.
- 연도는 2000부터 2099까지 허용합니다.
- 월은 01부터 12까지 허용합니다.
- 일은 01부터 31까지 허용합니다.
4. 확장자
- .jpg, .png, .csv 중 하나만 허용합니다.
5. 기타
- 각 항목은 반드시 _로 구분합니다.
- 공백과 한글은 허용하지 않습니다.
- 파일명 전체가 규칙에 일치해야 합니다.

# 검사 예시
| 입력                                                      | 결과 |
|-----------------------------------|------|
| train_cat01_20261105.jpg  | True |
| test_dog123_20260115.png  | True |
| valid_data01_20261231.csv | True |
| train_cat_20261105.jpg       | False |
| train_Cat01_20261105.jpg   | False |
| test_admin01_20261105.csv | False |
| sample_cat01_20261105.jpg | False |
| train_cat01_20261305.jpg   | False |
| train_cat01_20261132.jpg   | False |
| train_cat01_19991105.jpg   | False |
| train_cat01_20261105.gif   | False |
| train_cat01_2026115.jpg     | False |

# 구현 조건
re 모듈을 사용하세요.
정규표현식은 하나만 작성하세요.
그룹 ()과 OR 연산자 |를 활용하세요.
긍정 전방 탐색 (?=...)을 사용하세요.
부정 전방 탐색 (?!...)을 사용하세요.
re.fullmatch()로 파일명 전체를 검사하세요.

# 시작 코드
import re

filename = input("파일명 입력 : ")

regexp = r""  # 정규표현식 작성

result = re.fullmatch(regexp, filename)

print(bool(result))


# 추가 도전 문제
기본 문제를 완성했다면 다음 조건을 추가해 보세요.

1. .csv 파일은 train, test, valid 모두 허용하지만, .jpg, .png 파일은 train, test만 허용하도록 변경하세요.

참고: 기본 문제의 날짜 검사는 정규표현식으로 연도·월·일의 범위만 확인합니다. 실제 달력에 존재하는 날짜인지까지 보장하지는 않습니다.
"""


import re

filename = input("파일명 입력 : ")

regexp = r"^(train|test|valid)_((?=[^_]*?[0-9])(?!.*?admin)[a-z0-9]{3,15})_((20[0-9][0-9])(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01]))\.(jpg|png|csv)$" # 정규표현식 작성

result = re.fullmatch(regexp, filename)

print(bool(result))