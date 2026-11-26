"""
# Seaborn 실습 — 생산 실적 분석 및 시각화

파일명 : `27_차트실습.py`

한 제조업체에서 A, B, C 생산라인의 날짜별 생산량과
불량개수를 관리하고 있습니다.

주어진 데이터를 이용하여 다음 요구사항을 해결하세요.

```py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    "날짜": ["11/21", "11/22", "11/23", "11/24", "11/25"] * 3,
    "생산라인": ["A"] * 5 + ["B"] * 5 + ["C"] * 5,
    "생산량": [
        1200, 1500, 1300, 1800, 2000,
        1000, 1300, 1600, 1400, 1700,
        1800, 1600, 1900, 2100, 2200
    ],
    "불량개수": [
        12, 15, 8, 10, 7,
        20, 18, 15, 12, 10,
        30, 25, 20, 15, 11
    ]
})

```

# 요구사항

1. 날짜별 전체 생산량을 막대그래프로 표시하세요.
   - 날짜마다 다른 색상 적용
   - 막대 위에 생산량 표시

2. 날짜별 전체 생산량을 선그래프로 표시하세요.
   - 원형 마커 사용
   - 각 데이터 위치에 생산량 표시

3. 생산라인별 총 불량개수를 막대그래프로 표시하세요.
   - 생산라인마다 다른 색상 적용
   - 불량개수가 많은 생산라인부터 표시
   - 막대 위에 불량개수 표시

4. 날짜별 불량개수의 변화를 선그래프로 표시하세요.
   - 생산라인별로 서로 다른 색상 적용
   - 범례 표시
   - 사각형 마커 사용

5. 생산량과 불량개수를 이용하여 다음 열을 생성하세요.
   - 정상개수 : 생산량 - 불량개수
   - 불량률 : 불량개수 / 생산량 * 100

6. 생산라인별 전체 불량률을 막대그래프로 표시하세요.
   - 전체 불량률 = 총 불량개수 / 총 생산량 * 100
   - 불량률이 높은 생산라인부터 표시
   - 수치는 소수점 둘째 자리까지 표시
   - 수치 뒤에 % 기호 표시

7. 날짜별 불량률의 변화를 선그래프로 표시하세요.
   - 생산라인별로 서로 다른 색상 적용
   - 각 데이터 위치에 불량률 표시
   - 수치는 소수점 둘째 자리까지 표시


# 공통 사항

- 기존에 배운 sns.set_theme() 공통 설정을 사용합니다.
- 모든 그래프는 각각 별도의 창에 표시합니다.
- 모든 그래프에 적절한 제목과 축 이름을 설정합니다.
- 오차 막대 및 오차 범위는 표시하지 않습니다.
- 생산량과 불량개수에는 천 단위 콤마를 표시합니다.
- 수치가 제목을 침범하지 않도록 여백을 설정합니다.
- 그래프의 색상, 너비, 선 두께는 자유롭게 설정합니다.
- 생성한 모든 그래프를 각각 PNG 파일로 저장합니다.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# 공통 디자인 설정
sns.set_theme(
    style="whitegrid",
    palette="pastel",
    font="Binggrae Taom",
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

# 데이터 설정
df = pd.DataFrame({
    # "날짜": ["11/21", "11/22", "11/23", "11/24", "11/25"] * 3,
    "날짜": [
        "11/21", "11/22", "11/23", "11/24", "11/25",
        "11/21", "11/22", "11/23", "11/24", "11/25",
        "11/21", "11/22", "11/23", "11/24", "11/25"
    ],
    # "생산라인": ["A"] * 5 + ["B"] * 5 + ["C"] * 5,
    "생산라인": [
        "A", "A", "A", "A", "A",
        "B", "B", "B", "B", "B",
        "C", "C", "C", "C", "C"
    ],
    "생산량": [
        1200, 1500, 1300, 1800, 2000,
        1000, 1300, 1600, 1400, 1700,
        1800, 1600, 1900, 2100, 2200
    ],
    "불량개수": [
        12, 15, 8, 10, 7,
        20, 18, 15, 12, 10,
        30, 25, 20, 15, 11
    ]
})

# 경로 구하기
folder = Path(__file__).resolve().parent / "chart"

# 1. 날짜별 전체 생산량을 막대그래프로 표시하세요.
#    - 날짜마다 다른 색상 적용
#    - 막대 위에 생산량 표시

# (1-1) 그룹 명령을 사용
quiz1 = df.groupby("날짜")["생산량"].sum()
print(quiz1)
quiz1 = quiz1.reset_index()
print(quiz1)
chart = sns.barplot(
    data=quiz1,
    x="날짜", y="생산량",
    errorbar=None,
    hue="날짜"
)
chart.set_title("날짜별 전체 생산량(1-1)", fontsize=25)
chart.set(xlabel="날짜", ylabel="생산량(개)")
for container in chart.containers:
    chart.bar_label(container, fmt="{:,}", padding=5)
chart.margins(y=0.25)
plt.savefig(folder / "27_chart_1_1.png")
# plt.show()

# (1-2) Seaborn 라이브러리의 집계기능을 사용
plt.figure()
chart = sns.barplot(
    data=df,
    x="날짜", y="생산량",
    estimator="sum", #집계 기능 ON
    errorbar=None,
    hue="날짜"
)
chart.set_title("날짜별 전체 생산량(1-2)", fontsize=25)
chart.set(xlabel="날짜", ylabel="생산량(개)")
for container in chart.containers:
    chart.bar_label(container, fmt="{:,}", padding=5)
chart.margins(y=0.25)
plt.savefig(folder / "27_chart_1_2.png")
# plt.show()

# 2. 날짜별 전체 생산량을 선그래프로 표시하세요.
#    - 원형 마커 사용
#    - 각 데이터 위치에 생산량 표시
plt.figure()
chart = sns.lineplot(
    data=df,
    x="날짜", y="생산량",
    errorbar=None,
    estimator="sum",
    marker="o",
    markersize=5,
    markerfacecolor = "#2d3436",  # 기호 색상
    markeredgecolor = "#b2bec3",  # 기호 테두리 색상
)
chart.set_title("날짜별 전체 생산량(2)", fontsize=25)
chart.set(xlabel="날짜", ylabel="생산량(개)")

for line in chart.lines:
    x = line.get_xdata()
    y = line.get_ydata()
    size = min(len(x), len(y))

    for i in range(size):
        chart.text(
            x[i], y[i], f"{y[i]:,.0f}",
            ha="center", va="bottom"
        )

plt.savefig(folder / "27_chart_2.png")
# plt.show()

# 3. 생산라인별 총 불량개수를 막대그래프로 표시하세요.
#    - 생산라인마다 다른 색상 적용
#    - 불량개수가 많은 생산라인부터 표시
#    - 막대 위에 불량개수 표시
plt.figure() # 수동 리셋 코드
quiz3 = df.groupby("생산라인")["불량개수"].sum()
print(quiz3)
quiz3 = quiz3.sort_values(ascending=False)
print(quiz3)

chart = sns.barplot(
    data=df,
    x="생산라인", y="불량개수",
    errorbar=None,
    estimator="sum",
    order=quiz3.index, # 표시 순서를 알려주는 것
    hue="생산라인",
    width=0.5
)
chart.set_title("생산라인별 전체 불량개수", fontsize=25)
chart.set(xlabel="생산라인", ylabel="불량개수(개)")
for container in chart.containers:
    chart.bar_label(container, fmt="{:,}", padding=5)
chart.margins(y=0.25)
plt.savefig(folder / "27_chart_3.png")
# plt.show()

# 4. 날짜별 불량개수의 변화를 선그래프로 표시하세요.
#    - 생산라인별로 서로 다른 색상 적용
#    - 범례 표시
#    - 사각형 마커 사용
plt.figure()
chart = sns.lineplot(
    data=df,
    x="날짜", y="불량개수",
    errorbar=None,
    hue="생산라인", # 생산라인별로 데이터를 묶어서 관리
    # marker="s",
    style="생산라인", markers=["o", "s", "^"], dashes=False,
    # legend=False, #범례 제거
)
chart.set_title("날짜별 생산라인 불량현황", fontsize=25)
chart.set(xlabel="날짜", ylabel="불량개수(개)")
plt.savefig(folder / "27_chart_4.png")
# plt.show()

# 5. 생산량과 불량개수를 이용하여 다음 열을 생성하세요.
#    - 정상개수 : 생산량 - 불량개수
#    - 불량률 : 불량개수 / 생산량 * 100
df["정상개수"] = df["생산량"] - df["불량개수"]
df["불량률"] = df["불량개수"] / df["생산량"] * 100

# 6. 생산라인별 전체 불량률을 막대그래프로 표시하세요.
#    - 전체 불량률 = 총 불량개수 / 총 생산량 * 100
#    - 불량률이 높은 생산라인부터 표시
#    - 수치는 소수점 둘째 자리까지 표시
#    - 수치 뒤에 % 기호 표시
quiz6 = df.groupby("생산라인")[["생산량", "불량개수"]].sum()
print(quiz6)
quiz6["불량률"] = quiz6["불량개수"] / quiz6["생산량"] * 100
print(quiz6)
quiz6 = quiz6.sort_values("불량률", ascending=False)
print(quiz6)
quiz6 = quiz6.reset_index()
print(quiz6)

plt.figure()
chart = sns.barplot(
    data=quiz6,
    x="생산라인", y="불량률",
    errorbar=None,
    hue="생산라인",
    legend=False,
)
chart.set_title("생산라인별 전체 불량률", fontsize=25)
chart.set(xlabel="생산라인", ylabel="불량률(%)")

# 불량률을 형식에 맞춰 표시
# for container in chart.containers:
#     chart.bar_label(container, fmt="{:.2f}%", padding=5)

# 만약 불량률과 불량개수를 같이 표시하고 싶다면... 미리 계산해서 표시
xlabels = chart.get_xticklabels() # 차트의 x축 라벨 추출
# for xlabel in xlabels: # xlabels에서 하나씩 꺼내서 xlabel에 넣어
for i in range(len(xlabels)): # xlables의 개수만큼 0부터 시작해
    xlabel = xlabels[i]
    line = xlabel.get_text() # 라벨에서 생산라인명을 꺼내서
    condition = quiz6["생산라인"] == line # 같은 데이터를 찾고
    find = quiz6[condition] # 필터링해낸다
    text = f"{find["불량률"].iloc[0]:.2f}% ({find["불량개수"].iloc[0]:,.0f}개)"
    chart.bar_label(chart.containers[i], labels=[text], padding=5)
plt.savefig(folder / "27_chart_6.png")
# plt.show()

# 7. 날짜별 불량률의 변화를 선그래프로 표시하세요.
#    - 생산라인별로 서로 다른 색상 적용
#    - 각 데이터 위치에 불량률 표시
#    - 수치는 소수점 둘째 자리까지 표시
plt.figure()

chart = sns.lineplot(
    data=df,
    x="날짜", y="불량률",
    errorbar=None,
    hue="생산라인",
    marker="s",
)
chart.set_title("날짜별 생산라인 불량률", fontsize=25)
chart.set(xlabel="날짜", ylabel="불량률(%)")
for line in chart.lines: # 총 3번(생산라인 개수만큼)
    x = line.get_xdata()
    y = line.get_ydata()
    size = min(len(x), len(y))

    for i in range(size): # 각 생산라인의 데이터 수만큼 반복
        chart.text(
            x[i], y[i], f"{y[i]:.2f}%",
            ha="center", va="bottom"
        )

plt.savefig(folder / "27_chart_7.png")
plt.show()






