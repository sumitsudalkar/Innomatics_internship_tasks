import numpy as np
n = int(input().strip())
marr1 = np.array([[int(x) for x in input().strip().split()] for _ in range(n)])
narr2 = np.array([[int(x) for x in input().strip().split()] for _ in range(n)])

print(np.dot(marr1, narr2))
