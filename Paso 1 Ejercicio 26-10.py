import pymc as pm
import matplotlib.pyplot as plt 
import numpy as np

# Datos recta
t = np.arange(10000) / 1000  
m_true = 1.5  
b_true = 2.0  
y_true = m_true * t + b_true  

# Ruido
gaussian_noise = np.random.normal(size=t.shape[0])
observed_signal = y_true + gaussian_noise  

with pm.Model() as model:
    
    # Parámetros de la recta
    m = pm.Normal('m', mu=1.0, sigma=1.0)  # Distribución pendiente
    b = pm.Normal('b', mu=0.0, sigma=1.0)  # Distribución intersección
    sigma = pm.HalfNormal('sigma', sigma=1.0)  # Desviación ruido

    # Valor esperado de la señal (recta estimada)
    y_est = m * t + b

    # Likelihood: asumiendo ruido gaussiano
    y_obs = pm.Normal('y_obs', mu=y_est, sigma=sigma, observed=observed_signal)

    # Muestreamos del posterior
    trace = pm.sample(5000, return_inferencedata=True, chains=2, target_accept=0.9, tune=2000)

# Trazamos los resultados
pm.plot_trace(trace)
plt.show()
summary = pm.summary(trace)
print(summary)
