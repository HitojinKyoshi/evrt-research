import numpy as np
import matplotlib.pyplot as plt

# Simple illustrative model (NOT a physical prediction)
x = np.linspace(0, 10, 200)
y = np.exp(-0.2 * x) * np.sin(2 * x)

plt.plot(x, y)
plt.title("EVRT Toy Model Response (Illustrative)")
plt.xlabel("Parameter")
plt.ylabel("Response")
plt.grid()
plt.show()
