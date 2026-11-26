"""
Seaborn 라이브러리

Matplotlib를 바탕으로 동작하며,
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

# Seaborn 테마 설정 : 내부적으로 rcParam을 변경함
sns.set_theme(
    style="whitegrid",
    palette="pastel",
    # font="Malgun Gothic",
    font="Binggrae",
    rc={
        "axes.unicode_minus": False,
        "axes.titlesize": 20,
        "axes.titleweight": "bold",
        "axes.titlepad": 15,
        "axes.labelsize": 12,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.left": False,
        "axes.spines.bottom": False,
        "axes.ymargin": 0.2,
        "grid.linestyle": "--",
        "grid.alpha": 0.3,
        "figure.figsize": (10, 6),
        "figure.autolayout": True,
        "savefig.dpi": 150
    }
)

# 차트 표시
result = sns.barplot(
    data=products, # 데이터프레임
    x="상품명", # pandas의 컬럼명
    y="판매량", # pandas의 컬럼명
    errorbar=None, #오차 막대의 표시를 하지 않도록 설정
    hue="상품명", #색상을 적용시킬 기준 항목
)
result.set_title("상품별 판매량", fontsize=20)
result.set(
    xlabel="상품 이름", # 이미지에 표시될 X축 제목
    ylabel="판매량(개)" # 이미지에 표시될 Y축 제목
)
for container in result.containers:
    result.bar_label(container, fmt="{:,}", padding=5)
result.margins(y=0.25) #y축 25% 여백 추가

plt.show()
