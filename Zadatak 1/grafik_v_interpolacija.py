import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

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

# Kreiramo interpolator (linearna interpolacija)
interpolator = interp1d(valid_n, valid_v_n, kind='linear', fill_value="extrapolate")

# Kreiramo novi niz n za interpolaciju (sve vrednosti između -15 i 20, sa manjim korakom)
n_interp = np.arange(-15, 20, 3)  # Samo tačke deljive sa 3

# Računamo interpolisane vrednosti
v_interp = interpolator(n_interp)

# Crtamo originalni signal i interpolisane vrednosti
plt.figure(figsize=(10, 6))

# Originalni diskretni signal (tačke gde je signal definisan)
plt.stem(valid_n, valid_v_n, label='Originalni signal v[n]', basefmt=" ")

# Interpolisani signal
plt.plot(n_interp, v_interp, label='Interpolisani signal v[n] (linearna interpolacija)', color='orange')

# Podešavanje izgleda grafa
plt.xlabel('n')
plt.ylabel('v[n]')
plt.title('Grafik originalnog i interpolisanog signala v[n]')
plt.legend()
plt.grid(True)
plt.show()
