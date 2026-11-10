"""
그룹 처리와 OR 계산
"""

import re

input = "사과" # 사용자 입력

# regexp = "사과 또는 포도 또는 바나나"
regexp = r"^(사과|포도|바나나)$"

result = re.fullmatch(regexp, input)

if result is not None:
    print("참 잘했어요")
else:
    print("허용되지 않은 입력")