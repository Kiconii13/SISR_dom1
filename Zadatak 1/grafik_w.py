import numpy as np
import matplotlib.pyplot as plt

# Definišemo opseg za n
n = np.arange(-5, 10)

# Definišemo diskretnu Heavisideovu funkciju
def u(n):
    return np.where(n >= 0, 1, 0)

def w(n):
    return np.power(2.0, -n) * (u(n + 1) - u(n - 3))

# Računamo w[n] prema datoj formuli koristeći np.power za negativne eksponente
w_n = w(n)

# Crtamo grafik
plt.stem(n, w_n)
plt.xlabel('n')
plt.ylabel('w[n]')
plt.title(r'Grafik diskretnog signala $w[n] = 2^{-n} \cdot (u[n+1] - u[n-3])$')
plt.grid(True)
plt.show()
