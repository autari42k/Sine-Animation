import matplotlib.pyplot as plt
import random

x_vals = []
y_vals = []

x = random.randint(0, 10)
y = random.randint(100, 200)

fig, ax = plt.subplots()

ax.set_title("Liz's Aura")
ax.set_xlabel("Age")
ax.set_ylabel("Aura Level")
ax.grid(True)


for i in range(100):
    
    x += 2
    y *= 2

    x_vals.append(x)
    y_vals.append(y)

    ax.plot(x_vals, y_vals, color='blue')
    plt.ylim(0, 500)
    plt.xlim(0, 100)
    

    plt.pause(0.1)

plt.show()