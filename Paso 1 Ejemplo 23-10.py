import pymc as pm
import matplotlib.pyplot as plt 
import numpy as np

t = np.arange(10000)/1000
y_true = 3.0 * np.sin(2 * t + 0.5 * np.pi)
gaussian_noise = np.random.normal(size = t.shape[0])
observed_signal = y_true + gaussian_noise

with pm.Model() as model:
    
    A = pm.Normal('A', mu=3.0, sigma=1.0)      
    f = pm.Normal('f', mu=2.0, sigma=1.0)      
    phi = pm.Uniform('phi', lower=0, upper=2*np.pi)
    sigma = pm.HalfNormal('sigma', sigma=1.0)  

    # Expected value of the signal
    y_est = A * pm.math.sin(f * t + phi)

    # Likelihood: assuming Gaussian noise
    y_obs = pm.Normal('y_obs', mu=y_est, sigma=sigma, observed=observed_signal)

    # Sample from the posterior
    trace = pm.sample(5000, return_inferencedata=True, chains=4,target_accept=0.9,tune=2000)

    
pm.plot_trace(trace)
plt.show()
summary = pm.summary(trace)
print(summary)
