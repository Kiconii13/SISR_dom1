import numpy as np
import matplotlib.pyplot as plt
from grafik_x import x

def f(t):

    # x(t) -> t = -1 - 3*t
    result = x(-1-3*t)
    # Kombinacija oba dela
    return result


# Definišemo opseg za t
t = np.linspace(-2, 3, 1000)

# Izračunavamo f(t)
f_t = f(t)

# Crtamo grafik
plt.plot(t, f_t, label=r'$f(t) = x(-1-3t)$')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Grafik funkcije f(t)')
plt.legend()
plt.grid(True)
plt.show()
