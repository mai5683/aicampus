"""
다음 데이터를 막대그래프로 표시하세요.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Matplotlib 한글 설정
plt.rcParams["font.family"] = "Binggrae"
plt.rcParams["font.size"] = "16"
plt.rcParams["axes.unicode_minus"] = False

# 차트에 표시할 데이터
products = pd.DataFrame({
    "상품명": ["키보드", "마우스", "모니터", "헤드셋"],
    "판매량": [35, 60, 20, 45]
})

# 차트에 표시할 기본 설정
plt.figure(figsize=(6, 5))

# 막대그래프 생성
plt.bar(products["상품명"], products["판매량"], color="#F59A8A")

# 제목 및 축 이름 설정
plt.title("상품그래프")
plt.xlabel("상품명")
plt.ylabel("판매량(개)")

# (추가) 차트 데이터를 이미지로 저장 (차트 표시 전)
folder = Path(__file__).resolve().parent / "chart"
folder.mkdir(exist_ok=True)
plt.savefig(folder / "product_sales.png")

# 화면을 타이트하게 조정
plt.tight_layout()

# 그래프 표시
plt.show()

print("프로그램 종료")


