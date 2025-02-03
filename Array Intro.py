import numpy as np
import matplotlib.pyplot as plt
import random
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b[1][:] = 0
print(b)
a = np.array([1,2,3])
print(np.flip(a))
print(np.arange(1))
print(a)
print(len(a))
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
c = np.array([[np.zeros(2)],[np.zeros(2)]])

print(b[0][1])
print(b)
print(c)
a = 3*a
print(a)
a -= 1
print(a)

d = 5
d -= 1-3
print(d)
print(isinstance(d/5,int))
print(random.choices([0, 1], weights=[4, 1], k=0))
print(len(np.argwhere(a == 2)))
print(3**2)

print(random.choices([0, 1], weights=[7, 3]))

Turn = np.array(random.choices([-1, 0, 1], weights=[2 * 5, 3 * 5, 2*0],k=3))
print(Turn)
print(np.argwhere(Turn == 1))
print(len(np.argwhere(Turn == 1)))

d = [1, 2]
print()