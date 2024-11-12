import numpy as np
import matplotlib.pyplot as plt
from pycbc.waveform import get_td_waveform
from scipy.optimize import minimize

# Simular señal observada (incluye ruido)
np.random.seed(42)
t = np.linspace(0, 1, 4096)  # Tiempo en segundos
hp_rom = 10 * np.sin(2 * np.pi * 100 * t)  # Señal original simulada (onda sinusoidal)
gaussian_noise = np.random.normal(scale=2, size=t.shape[0])
observed_signal = hp_rom + gaussian_noise

# Función para generar una señal modelo sin incluir la distancia
def generate_model_signal(mass1, mass2, approximant="SEOBNRv4"):
    hp, _ = get_td_waveform(approximant=approximant,
                            mass1=mass1,
                            mass2=mass2,
                            delta_t=1.0/4096,
                            f_lower=20.0)
    hp_np = np.array(hp)  # Convertimos a array de Numpy
    return hp_np / np.max(np.abs(hp_np))  # Normalizamos la señal

# Función de error entre la señal observada y la generada
def error_function(params):
    mass1, mass2 = params
    model_hp = generate_model_signal(mass1, mass2)
    
    # Interpolar para que coincidan los tiempos
    observed_resampled = np.interp(np.linspace(0, len(model_hp)/4096, len(model_hp)), t, observed_signal)
    
    # Normalizar la señal observada
    observed_resampled /= np.max(np.abs(observed_resampled))
    
    # Calcular el error como suma de diferencias cuadráticas
    return np.sum((observed_resampled - model_hp)**2)

# Parámetros iniciales y límites
initial_guess = [30, 30]  # [mass1, mass2]
bounds = [(5, 50), (5, 50)]  # Límites para los parámetros

# Optimización
result = minimize(error_function, initial_guess, bounds=bounds)

# Recuperar parámetros óptimos
mass1_opt, mass2_opt = result.x

# Generar la señal ajustada con los parámetros óptimos
best_fit_signal = generate_model_signal(mass1_opt, mass2_opt)

# Interpolar para graficar
observed_resampled = np.interp(np.linspace(0, len(best_fit_signal)/4096, len(best_fit_signal)), t, observed_signal)
observed_resampled /= np.max(np.abs(observed_resampled))  # Normalizar la señal observada

# Crear los gráficos separados
plt.figure(figsize=(12, 10))

# Señal observada
plt.subplot(3, 1, 1)
plt.plot(t, observed_signal, label="Señal Observada (con Ruido)", color='blue', alpha=0.7)
plt.title("Señal Observada")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

# Señal original simulada
plt.subplot(3, 1, 2)
plt.plot(t, hp_rom / np.max(np.abs(hp_rom)), label="Señal Original (Simulada)", color='green', linestyle=':')
plt.title("Señal Original Simulada")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud Normalizada")
plt.grid()

# Señal ajustada
plt.subplot(3, 1, 3)
plt.plot(np.linspace(0, len(best_fit_signal)/4096, len(best_fit_signal)), best_fit_signal, label="Señal Ajustada", color='red', linestyle='--')
plt.title("Señal Ajustada")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud Normalizada")
plt.grid()

plt.tight_layout()
plt.show()
