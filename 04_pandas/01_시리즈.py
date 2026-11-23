"""
Pandas
- 파이썬에서 표 형태의 데이터를 쉽게 관리하고 분석하기 위해 만들어진 라이브러리
- NumPy와 용도를 구분할 필요가 있다.
- 설치 필요 : [python -m] pip install pandas
"""

import numpy as np
import pandas as pd

# 비교를 위해 점수 다섯 개를 동일하게 NumPy와 Series로 저장한 뒤 작업을 해보자.

scores = [55, 65, 72, 80, 81]
arr = np.array(scores)      # NumPy의 생성 방식
series = pd.Series(scores)
print("numpy", arr)
print("pandas", series)
print(type(arr), type(series))

# series를 만들 떄 데이터에 "인덱스"를 부여할 수 있다.
named = pd.Series(scores, index=["피카츄", "라이츄", "파이리", "꼬부기", "버터플"])
print("pandas(named)", named)

print()
# 접근 방법의 차이 비교

# numpy는 숫자인덱스 사용
print(arr[0], arr[1], arr[2], arr[3], arr[4])

# series도 별도의 인덱스를 설정하지 않은 경우 숫자인덱스 사용 가능
print(series[0], series[1], series[2], series[3], series[4])
# 인덱스를 설정하는 순간 해당 인덱스로 접근하는 것이 기본값이 됨
# print(named[0], named[1])
print(named["피카츄"], named["라이츄"], named["파이리"], named["꼬부기"], named["버터플"])
print(named.loc["피카츄"], named.loc["라이츄"])

# Pandas를 쓰게 되면 데이터가 단순 순서가 아닌 구조화된 형태로 사용 가능
# 하지만 기존처럼도 이용 가능
print(named.iloc[0], named.iloc[1], named.iloc[2], named.iloc[3], named.iloc[4])

# 결국 배열을 분석한다는 건...
# 합계, 평균, 표준편차, 최대, 최소 혹은 조건에 따른 필터링

# (ex) 80점 이상인 학생들의 점수만 출력
print(arr[arr>=80])         # numpy
print(series[series>=80])   # pandas
print(named[named>=80])     # pandas

print(np.sum(arr))          # numpy 방식 합계
print(series.sum())         # series 합계
print(named.sum())          # 인덱스와 무관

# 최대, 최소, 평균, 표준편차
print("최대값", np.max(arr), series.max(), named.max())
print("최소값", np.min(arr), series.min(), named.min())
print("평균", np.mean(arr), series.mean(), named.mean())
# 표준편차는 구하는 방식의 차이로 약간의 차이 발생
# (numpy는 모집단, pandas는 표본집단을 대상으로 구함)
print("표준편차", np.std(arr), series.std(), named.std())


