import matplotlib.pyplot as plt
import sympy as smp
import numpy as np

init = 80
g = 9.81
bounce = 0.8      # energy loss factor

plt.ion()

y = init
v = 0
dt = 0.05

fig = plt.figure(1)

for i in range(1, 1000):

    if not plt.fignum_exists(1):
        break

    v -= g * dt
    y += v * dt

    if y <= 0:
        y = 0
        v = -v * bounce
    

    plt.cla()
    plt.plot(0, y, 'o')
    plt.ylim(0, init + 5)
    plt.xlim(-1, 1)

    

    plt.pause(0.001)

plt.ioff()
plt.close('all')