import numpy as np
import matplotlib.pyplot as plt
from grafik_x import x

# Definicija funkcije g(t)
def g(t):
    return x(3-t/4)


# Definišemo opseg za t
t = np.linspace(0, 18, 1000)

# Izračunavamo g(t)
g_t = g(t)

# Crtamo grafik
plt.plot(t, g_t, label=r'$g(t) = x(\left(3 - \frac{t}{4}\right)) $')
plt.xlabel('t')
plt.ylabel('g(t)')
plt.title('Grafik funkcije g(t)')
plt.legend()
plt.grid(True)
plt.show()
