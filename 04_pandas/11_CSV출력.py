"""
데이터프레임(DataFrame)을 CSV로 출력(=저장)하기
"""


import pandas as pd
from pathlib import Path

df = pd.DataFrame(
    {
        "no" : [4, 7, 25],
        "name" : ["파이리", "꼬부기", "피카츄"],
        "type" : ["불꽃", "물", "전기"]
    }
)

print(df,"\n")

# dir = Path("./data")
# dir.mkdir(exist_ok=True)
Path("./data").mkdir(exist_ok=True)     # 디렉터리 생성

# DataFrame을 CSV로 내보내기
df.to_csv("./data/monsters.csv", encoding="utf-8-sig", index=False)

print("csv 저장 완료")
