import numpy as np
import matplotlib.pyplot as plt


# Definišemo Heaviside-ovu funkciju u(t)
def u(t):
    return np.where(t >= 0, 1, 0)


# Definišemo x(t) = u(1 - t^2) * (t^2 - 1) + (u(2 - t) - u(1 - t)) * (t - 1)
def x(t):
    return u(1 - t ** 2) * (t ** 2 - 1) + (u(2 - t) - u(1 - t)) * (t - 1)


# Definišemo y(t) = -u(-t) * u(t + 2) + 2 * u(t) * u(1 - t)
def y(t):
    return -u(-t) * u(t + 2) + 2 * u(t) * u(1 - t)


# Funkcija za numeričku integraciju konvolucije koristeći što precizniju podelu
def convolution_integral(t):
    # Podeljujemo interval na mnogo manjih delova za precizniju integraciju
    num_points = 1000  # Povećali smo broj tačaka za preciznost
    tau_values = np.linspace(-10, 10, num_points)  # Vrednosti tau na opsegu [-10, 10]

    # Računamo vrednosti funkcije x(tau) i y(t - tau) za svaki tau
    x_values = x(tau_values)
    y_values = y(t - tau_values)

    # Izračunavamo konvoluciju koristeći metodu trapeznog pravila
    result = np.sum(x_values * y_values) * (tau_values[1] - tau_values[0])  # Množimo sa veličinom koraka
    return result


# Evaluiramo c(t) za opseg t vrednosti
t_values = np.linspace(-3, 3, 100)  # Opseg vrednosti t
c_values = [convolution_integral(t) for t in t_values]  # Računanje vrednosti konvolucije

# Prikazujemo rezultat u grafiku
plt.plot(t_values, c_values, label="c(t) = x(t) * y(t)")
plt.xlabel("t")
plt.ylabel("c(t)")
plt.title("Konvolucija x(t) i y(t)")
plt.legend()
plt.grid(True)
plt.show()
