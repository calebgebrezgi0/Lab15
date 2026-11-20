"""
Program Name: Math Formula Plotter
Author: Caleb Gebrezgi
Purpose: Plot a sine wave using matplotlib.
Date: November 20, 2026
"""


import math
import matplotlib.pyplot as plt

x = [i * 0.1 for i in range(300)]
y = [math.sin(value) for value in x]

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")

plt.savefig("sine_wave.png")
plt.show()