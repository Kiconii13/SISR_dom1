import numpy as np
import matplotlib.pyplot as plt

# Definišemo diskretnu Heavisideovu funkciju
def u(n):
    return np.where(n >= 0, 1, 0)

# Definicija funkcije w[n]
def w(n):
    return np.power(2.0, -n) * (u(n + 1) - u(n - 3))

# Definicija parnog dela w[n]
def w_paran(n):
    return (w(n) + w(-n)) / 2

# Definicija neparnog dela w[n]
def w_neparan(n):
    return (w(n) - w(-n)) / 2

# Definišemo opseg za n
n = np.arange(-15, 20)

# Računamo w[n], w_paran[n] i w_neparan[n]
w_n = w(n)
w_paran_n = w_paran(n)
w_neparan_n = w_neparan(n)

# Crtamo sve tri funkcije
plt.figure(figsize=(10, 6))

# Signal w[n]
plt.stem(n, w_n, label='Signal w[n]', basefmt=" ")

# Parni deo signala w[n]
plt.stem(n, w_paran_n, label='Parni deo w[n]', linefmt='g', markerfmt='go', basefmt=" ")

# Neparni deo signala w[n]
plt.stem(n, w_neparan_n, label='Neparni deo w[n]', linefmt='r', markerfmt='ro', basefmt=" ")

# Podešavanje izgleda grafa
plt.xlabel('n')
plt.ylabel('w[n], w_paran[n], w_neparan[n]')
plt.title('Grafik signala w[n], parnog i neparnog dela')
plt.legend()
plt.grid(True)
plt.show()
