import numpy as np
import matplotlib.pyplot as plt

# Definicija funkcije x(t) prema prethodnim rezultatima
def x(t):
    # Prvi deo: u(1 - t^2) * (t^2 - 1)
    part1 = np.heaviside(1 - t ** 2, 1) * (t ** 2 - 1)

    # Drugi deo: (u(2 - t) - u(1 - t)) * (t - 1)
    part2 = (np.heaviside(2 - t, 1) - np.heaviside(1 - t, 1)) * (t - 1)

    # Kombinacija oba dela
    return part1 + part2


# Definišemo opseg za t
t = np.linspace(-2, 3, 500)

# Kombinacija oba dela
x_t = x(t)

# Crtamo grafik
plt.plot(t, x_t, label=r'$x(t) = u(1 - t^2) \cdot (t^2 - 1) + (u(2 - t) - u(1 - t)) \cdot (t - 1)$')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Grafik funkcije x(t)')
plt.legend()
plt.grid(True)
plt.show()
