import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# plot data
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sinusoidal Wave")
plt.show()
