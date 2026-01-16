import sympy as smp
import matplotlib.pyplot as plt
import numpy as np
import random

x = smp.symbols('x')
b = random.randint(1, 5)
y = smp.sin(x) + b

y_f = smp.lambdify(x, y) 
p = random.randint(1, 60)
d = 2

fig = plt.figure(1)

for i in range(p):

    if not plt.fignum_exists(1):
        break
    
    if i % 2 == 0:
        d += 5
    x_num = np.linspace(0, i, d)
    plt.plot(x_num, y_f(x_num), color='black')
    plt.pause(0.1)
    print(f'i:{i}, d:{d}')


plt.show()
