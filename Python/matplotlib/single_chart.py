import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 10000)
a = np.sin(x)
b = np.cos(x)
c = np.tan(x)
d = np.log(x)

plt.figure(figsize=(8, 4))
plt.plot(x, a, label="$sin(x)$", color="green", linewidth=1)
plt.plot(x, b, label="$cos(x)$", color='blue', linewidth=1)
plt.plot(x, c, "b--", label="$tan(x)$", color='red', linewidth=1)
plt.plot(x, d, "b--", label="$log(x)$", color='grey', linewidth=1)

plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot -> Study!")
plt.xlim(-10, 10)
plt.ylim(-5, 5)
plt.legend()
plt.show()
