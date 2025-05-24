import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# Parametros del sistema M/M/c
mu = 4  # Tasa de servicio por servidor
c = 3   # Numero de servidores

# Funcion para calcular P0 (probabilidad de cero clientes en el sistema)
def calcular_P0(lambda_val, mu, c):
    rho = lambda_val / (c * mu)
    if rho >= 1:
        # El sistema es inestable, P0 no se puede calcular en estado estacionario
        return np.nan 

    sumatoria = 0
    for n in range(c):
        sumatoria += (lambda_val / mu)**n / factorial(n)
    
    sumatoria += ((lambda_val / mu)**c) / (factorial(c) * (1 - rho))
    P0 = 1 / sumatoria
    return P0

# Funcion para calcular Lq (longitud promedio de la cola)
def calcular_Lq(lambda_val, mu, c):
    rho = lambda_val / (c * mu)
    if rho >= 1:
        return np.nan  # El sistema es inestable, la longitud de la cola tiende a infinito
    
    P0 = calcular_P0(lambda_val, mu, c)
    if np.isnan(P0): # Manejar casos donde P0 podria ser NaN debido a rho >= 1
        return np.nan

    numerador = (lambda_val / mu)**c * lambda_val * mu
    denominador = factorial(c - 1) * (c * mu - lambda_val)**2
    Lq = (numerador / denominador) * P0
    return Lq

# Crear un rango de valores de lambda
lambda_vals = np.linspace(0.1, c * mu - 0.1, 100)

# Calcular Lq para cada valor de lambda
Lq_vals = np.array([calcular_Lq(l, mu, c) for l in lambda_vals])



### Graficas de Resultados




#### Grafica de $L_q$


plt.figure()
plt.plot(lambda_vals, Lq_vals, linewidth=2)
plt.xlabel('<span class="math-inline">\\lambda</span> (tasa de llegadas)')
plt.ylabel('<span class="math-inline">L\_q</span> (longitud promedio de la cola)')
plt.title('Longitud promedio de la cola <span class="math-inline">L\_q</span> en funcion de <span class="math-inline">\\lambda</span>')
plt.grid(True)
plt.show()
