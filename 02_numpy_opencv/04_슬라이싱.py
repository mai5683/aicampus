"""
numpy의 배열 슬라이싱

- numpy는 python과 동일한 방식의 슬라이싱을 제공
- 슬라이싱의 결과가 독립된 배열이 아니라 공유 뷰(view)를 반환
"""

import numpy as np

py_list = [10, 20, 30, 40, 50]
np_list = np.array([10, 20, 30, 40, 50])

# 인덱스 체계는 동일하다.
print(py_list[0], np_list[0])
print(py_list[1], np_list[1])
print(py_list[-1], np_list[-1])

# 슬라이싱 비교
py_slice = py_list[1:4]    # 4는 미포함
print(py_slice)

np_slice = np_list[1:4]    # 4는 미포함
print(np_slice)

# 슬라이싱 결과값을 변경하면?
py_slice[0] = 100   # 자른 결과의 [0]은 원본의 [1]
np_slice[0] = 100   # 자른 결과의 [0]은 원본의 [1]

print(py_list, py_slice)
print(np_list, np_slice)

# 결론 :
# - numpy는 슬라이싱을 해도 복사가 안 된다.
# - 명시적으로 복사 명령을 써야 한다. copy()
arr = np.array([10, 20, 30, 40, 50])
pcs = arr[1:4].copy()
pcs[0] = 100
print(arr, pcs)

# numpy는 다차원에서도 슬라이싱을 지원
data = np.zeros((3,3), dtype=int)


# data[1][1] = 10
# data[1][2] = 10
# data[2][1] = 10
# data[2][2] = 10
data[1:, 1:] = 10

print(data)

