"""
Matplotlib

데이터를 그래프로 표현하는 라이브러리
Pandas, OpenCV, NumPy 등으로 분석한 결과를 그래프로 표현해서 변화를 쉽게 확인

pip install matplotlib 설치
pip freeze > requirements.txt

- 막대 그래프(Bar Chart) : 항목별 크기 비교 (차이 확인)
- 꺾은 선 그래프(Line Chart) : 항목의 값 변화 확인
- 원 그래프(Pie Chart, Doughnut Chart) : 항목의 비중
"""

import pandas as pd
import matplotlib.pyplot as plt

# 차트에 표시할 기본 설정
plt.rcParams["font.family"] = "Malgun Gothic"   # 한글 지원 폰트 설정
plt.rcParams["axes.unicode_minus"] = False      # 그래프의 음수축 깨짐 방지

# 차트에 표시할 데이터
labels = ["A", "B", "C", "D"]
values = [12, 7, 18, 5]

# 그래프의 크기 설정 (단위 : inch)
plt.figure(figsize=(8, 5))

# 막대그래프 생성
plt.bar(labels, values, color="steelblue")

# 제목 및 축 이름 설정
plt.title("생산라인별 불량개수")
plt.xlabel("생산라인")
plt.ylabel("불량개수")

# 그래프 표시
plt.show()


