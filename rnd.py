import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)
y = np.sin(x) / x

plt.plot(x, y)
plt.title("y = sin(x) / x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
