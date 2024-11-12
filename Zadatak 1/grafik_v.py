import numpy as np
import matplotlib.pyplot as plt

# Definišemo diskretnu Heavisideovu funkciju
def u(n):
    return np.where(n >= 0, 1, 0)

# Definicija funkcije w[n]
def w(n):
    return np.power(2.0, -n) * (u(n + 1) - u(n - 3))

# Definicija funkcije v[n]
def v(n):
    valid_n = n % 3 == 0  # Samo vrednosti n koje su deljive sa 3
    v_n = np.zeros_like(n, dtype=float)  # Inicijalizujemo v_n kao nulu
    v_n[valid_n] = -3 * w(3 - n[valid_n] / 3)
    return v_n

# Definišemo opseg za n
n = np.arange(-3, 20)

# Računamo v[n]
v_n = v(n)

# Selektujemo samo tačke koje su deljive sa 3
valid_n = n[n % 3 == 0]
valid_v_n = v_n[n % 3 == 0]

# Crtamo samo diskretni signal
plt.figure(figsize=(10, 6))

# Originalni diskretni signal (tačke gde je signal definisan)
plt.stem(valid_n, valid_v_n, label='Signal v[n] (diskretni)', basefmt=" ")

# Podešavanje izgleda grafa
plt.xlabel('n')
plt.ylabel('v[n]')
plt.title('Grafik diskretnog signala v[n]')
plt.legend()
plt.grid(True)
plt.show()
