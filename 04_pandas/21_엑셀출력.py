"""
Excel 파일 출력

Excel은 CSV와 다르게 하나의 파일에 여러 시트와 서식 등을 담을 수 있습니다.
Pandas는 데이터프레임을 엑셀로 내보낼 수 있는 명령이 있습니다.

- 출력(저장) : df.to_excel()
- 입력(열기) : pd.read_excel()

[주요 옵션]
index=False             - 행 인덱스를 저장하지 않음
sheet_name="이름"        - 저장하거나 불러올 시트 이름을 지정
sheet_name=0            - 첫 번째 시트 지정 (기본값)

Excel 파일을 처리하기 위해서는 openpyxl 라이브러리가 필요합니다.

pip install openpyxl 또는 python -m pip install openpyxl 로 설치

만약 requirements.txt가 있다면 pip install -r requirements.txt 로 설치

현재 상태 라이브러리를 버전까지 자동으로 저장할 수 있다

pip freeze > requirements.txt
"""

# 저장할 데이터 준비
import pandas as pd

df = pd.DataFrame({
    "제품번호": ["P001", "P002", "P003", "P004"],
    "생산라인": ["A", "A", "B", "B"],
    "무게": [100.2, 99.8, 105.3, 100.1],
    "검사결과": ["정상", "정상", "불량", "정상"]
})

print(df, "\n")

# 경로 설정
from pathlib import Path
folder = Path(__file__).resolve().parent / "data"
folder.mkdir(exist_ok=True)

# 인코딩을 지정할 수 없다 (엑셀의 고유 방식으로 처리됨)
df.to_excel(
    folder / "inspection.xlsx", #저장할 위치
    index=False,                #인덱스 사용여부
    engine="openpyxl",          #내보낼 때 사용할 엔진(기술)명
    # sheet_name=0,               #기본시트1
    sheet_name="검사기록",        #시트이름 지정
)
print("엑셀 파일로 저장 완료")






