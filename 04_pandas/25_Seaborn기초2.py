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
    data=products,  # 데이터프레임
    x="상품명",     # pandas의 컬럼명
    y="판매량",     # pandas의 컬럼명
    errorbar=None,  # 오차 막대 표시를 하지 않도록 설정

    # color="#00b894"  # 모든 막대에 일괄 적용

    # 색상 패턴을 주기 위한 설정 (hue, palette가 세트로 설정됨)
    hue="상품명",   # 색상을 적용시킬 기준 항목
    # palette=["#F59A8A", "#38BC90", "#7A66DB", "#66BEDB"]  # 각각 색상 설정 가능
    palette="pastel",

    width=0.6,      # 막대 폭 비율 (0~1), 기본값 : 0.8
    saturation=1,   # 채도 (0~1), 1이면 원래색, 0이면 무채색
    alpha=1,        # 불투명도 (0~1), 1이면 완전 불투명, 0이면 투명
    edgecolor="black",  # 테두리 색상, None이면 테두리 없음
    linewidth=2,        # 테두리 두께 (단위 : pt)
)
# plt.title("상품별 판매량")
result.set_title("상품별 판매량", fontsize=20)
result.set(
    xlabel="상품 이름",     # 이미지에 표시될 X축 제목
    ylabel="판매량(개)"     # 이미지에 표시될 Y축 제목
)
# 막대그래프의 막대에 실제 수치를 기입
# - result.containers는 차트 내에서 관리되는 막대 그룹을 의미
# - hue를 지정하면 그룹이 여러 개가 됨.
# result.bar_label(result.containers[0])
# result.bar_label(result.containers[1])
# result.bar_label(result.containers[2])
# result.bar_label(result.containers[3])
for container in result.containers:
    result.bar_label(container, fmt="{:,.1f}", padding=5)
result.margins(y=0.25)  # y축 25% 여백 추가

plt.show()

