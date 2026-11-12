# 시드의 개념

import numpy as np

rng = np.random.default_rng(2)
first = rng.integers(0, 101, size=10, dtype=int)
print(first)

rng = np.random.default_rng(2)      # 위에 한 번만 쓰면 first와 second의 결과는 달라진다.
second = rng.integers(0, 101, size=10, dtype=int)
print(second)

third = rng.integers(0, 101, size=10, dtype=int)
print(third)