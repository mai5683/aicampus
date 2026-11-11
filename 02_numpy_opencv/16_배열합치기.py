"""
배열 합치기(병합)

- np.concatenate()
- np.hstack()   # 수평 방향
- np.vstack()   # 수직 방향
"""

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 튜플로 연결할 배열들을 묶어서 전달해야 한다.
# 괄호가 두 개 있는 것처럼 보이지만 의미가 다르다.
c = np.concatenate((a, b))
print(c)

# 1차원이라서 방향이 하나 밖에 없다. (axis=0, 한 줄(칸 방향))
d = np.concatenate((a, b), axis=0)
print(d)

# 간편하게 하려면 vstack()을 사용, 수직 방향 병합
e = np.vstack((a, b))
print(e)
print(e.shape)

# 수평도 쉬운 명령이 존재 - hstack()
f = np.hstack((a, b))
print(f)
print(f.shape)


# 2차원에서의 배열 병합
# - concatenate()에서는 axis=0 또는 1로 병합방향 지정 가능
# - hstack(), vstack() 가능
n1 = np.array([ [1, 2], [3, 4] ])
n2 = np.array([ [5, 6], [7, 8] ])

# concatenate()
# n3 = np.concatenate((n1, n2))      # ([n1, n2]) 처럼 리스트로 만들어도 된다.
# n3 = np.concatenate((n1, n2), axis=0)
n3 = np.concatenate((n1, n2), axis=1)
# n3 = np.concatenate((n1, n2), axis=2)    # 존재하지 않는 축
print(n3)
print(n3.shape)

# hstack(), vstack()
n4 = np.hstack((n1, n2))
n5 = np.vstack((n1, n2))
print(n4)
print(n4.shape)
print(n5)
print(n5.shape)

# 배열의 형태에 따라서 병합이 안 되는 경우도 있을까?
# - 줄이든 칸이든 병합하는 쪽의 크기가 맞아야 한다.
m1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
m2 = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

# m3 = np.concatenate((m1, m2))   # 안 됨
# m3 = np.vstack((m1, m2))    # 안 됨
# m3 = np.hastack((m1, m2))   # 안 됨

# 크기를 바꾸거나 회전하는 등 변화를 주어 합치면 된다.
# print(m2.reshape(2, 3))
m2_copy = m2.reshape(2, 3). copy()
m3 = np.hstack((m1, m2_copy))
m4 = np.vstack((m1, m2_copy))
print(m3)
print(m3.shape)
print(m4)
print(m4.shape)

print("--------------------------")
# 배열을 회전시킬 수 있다 (=테트리스처럼)
# 명령 : np.rot90(배열, 횟수)
print(m2)
print(np.rot90(m2))             # 반시계 90도
print(np.rot90(m2, 2))    # 반시계 180도
print(np.rot90(m2, -1))   # 시계방향 90도
print("--------------------------")

m2_rotate = np.rot90(m2, -1).copy()
m5 = np.hstack((m1, m2_rotate))
m6 = np.vstack((m1, m2_rotate))
print(m5, m5.shape)
print(m6, m6.shape)

