import numpy as np
from pathlib import Path

ab1 = Path("Data/ab/ab/ab1.npy")

np.load(ab1.as_posix())
print(np)
