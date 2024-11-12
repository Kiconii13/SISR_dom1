import numpy as np
import matplotlib.pyplot as plt

# Definisemo diskretnu step funkciju u[n]
def u(n):
    return np.where(n >= 0, 1, 0)

# Definisemo signal z[n] = u[n+4] - u[-n-1]
def z(n):
    return u(n + 4) - u(-n - 1)

# Definisemo signal w[n] = 2^(-n) * (u[n+1] - u[n-3)), koristeći decimalnu osnovu za eksponencijalni izraz
def w(n):
    return (2.0 ** (-n)) * (u(n + 1) - u(n - 3))

# Opseg n vrednosti za signale
n_values = np.arange(-10, 10)  # Opseg za posmatranje signala

# Računamo vrednosti z[n] i w[n] na definisanom opsegu
z_values = z(n_values)
w_values = w(n_values)

# Izračunavanje konvolucije između z[n] i w[n]
conv_values = np.convolve(z_values, w_values, mode='full')
conv_n_values = np.arange(2 * n_values[0], 2 * n_values[-1] + 1)  # Indeksi za konvoluciju

# Prikazivanje rezultata
plt.figure(figsize=(12, 8))


# Prikazivanje konvolucije z[n] * w[n]
plt.stem(conv_n_values, conv_values, basefmt=" ")
plt.title("Konvolucija z[n] * w[n]")
plt.xlabel("n")
plt.ylabel("z[n] * w[n]")
plt.grid(True)

# Prikazujemo grafike
plt.tight_layout()
plt.show()
