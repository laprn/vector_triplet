import numpy as np
from icecream import ic

A = np.array([[a1, a2, a3], [a4, a5, a6], [a7, a8, a9]])
ic(np.linalg.det(A))