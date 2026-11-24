"""
CSV 입력
"""

import pandas as pd

# 만약 index가 존재한다면 알려주면서 읽어야 한다.
df = pd.read_csv(
    "./data/monsters2.csv",
    index_col="name")

print(df)
