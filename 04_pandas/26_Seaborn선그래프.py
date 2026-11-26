"""
Seaborn 라이브러리로 꺾은 선 그래프 그리기

시간이나 순서에 따른 데이터의 변화 추세를 표현하는 방식의 그래프
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(
    style="whitegrid",
    palette="pastel",
    font="Malgun Gothic",
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

# 데이터 준비
df = pd.DataFrame({
    "날짜" : ["11/21", "11/22", "11/23", "11/24", "11/25"],
    "생산량" : [120, 150, 130, 180, 200]
})

# 차트 만들기
chart = sns.lineplot(
    data=df,    # 데이터프레임
    x="날짜",    # x축 데이터
    y="생산량",   # y축 데이터
    errorbar=None,
    # 차트의 디자인 속성
    marker="o",     # 기호 모양
    markersize=5,   # 기호 크기
    markerfacecolor="#2d3436",  # 기호 색상
    markeredgecolor="#b2bec3",  # 기호 테두리 색상
    markeredgewidth=2,          # 기호 테두리 두께
    linestyle="--",             # 선 스타일
    linewidth=2,                # 선 두께
    color="#74b9ff"             # 선 색상
)
chart.set_title("최근 5일간 생산량 변화", fontsize=25)
chart.set(xlabel="날짜", ylabel="생산량(개)")

# 라인 위에 수치 표시하기
for line in chart.lines:
    x = line.get_xdata()
    y = line.get_ydata()
    size = min(len(x), len(y))

    # chart.annotate(f"{y[0]}개", (x[0], y[0]))
    # chart.annotate(f"{y[1]}개", (x[1], y[1]))
    # chart.annotate(f"{y[2]}개", (x[2], y[2]))
    # chart.annotate(f"{y[3]}개", (x[3], y[3]))
    # chart.annotate(f"{y[4]}개", (x[4], y[4]))
    for i in range(size):
        chart.annotate(
            f"{y[i]}:,.0f",
            (x[i], y[i]),
            #글자의 위치를 아름답게 배치하기 위한 옵션
            ha="center",    # 수평정렬
            va="bottom",    # 수직정렬
            # 글자 미세조정
            xytext=(0, 10),
            textcoords="offset points"
        )

# 차트 표시
plt.show()