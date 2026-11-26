"""
Seaborn 라이브러리

Matplotlib을 바탕으로 동작하며,
여러 데이터 형태를 차트로 쉽게 표시하도록 도와주는 도구

설치 필요 : pip install seaborn
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 차트에 표시할 데이터
products = pd.DataFrame({
    "상품명": ["키보드", "마우스", "모니터", "헤드셋"],
    "판매량": [35, 60, 20, 45]
})

# Seaborn 테마 설정 : 내부적으로 rcParam을 변경함.
# - 가능한 테마 : darkgrid, whitegird, dark, white, ticks
sns.set_theme(style="darkgrid")

# Matplotlib 한글 설정
plt.rcParams["font.family"] = "Binggrae"
plt.rcParams["font.size"] = "16"
plt.rcParams["axes.unicode_minus"] = False

# 차트 표시
result = sns.barplot(
    data=products,
    x="상품명",     # pandas의 컬럼명
    y="판매량",     # pandas의 컬럼명
    errorbar=None
)
# plt.title("상품별 판매량")
result.set_title("상품별 판매량", fontsize=20)
result.set(
    xlabel="상품 이름",     # 이미지에 표시될 X축 제목
    ylabel="판매량(개)"     # 이미지에 표시될 Y축 제목
)
plt.show()

