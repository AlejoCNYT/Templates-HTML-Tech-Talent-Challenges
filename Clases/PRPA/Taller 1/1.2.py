import numpy as np

n = 10
r = 3

a = np.math.factorial(n)
b = np.math.factorial(n-r) * np.math.factorial(r)

c = a/b

print(c)
