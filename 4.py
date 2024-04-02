import numpy as np
import matplotlib.pyplot as plt 

cantidad_muestras=1000# cantidad de valores tiempo
x= np.linspace (-10,10,cantidad_muestras)
h= [np.exp(-x*x/2) * np.sin(x*0.99*2*np.pi), np.exp(-x*x/2) * np.sin(x*0.09*2*np.pi), np.exp(-x*x/2) * np.sin(x*0.21*2*np.pi), np.exp(-x*x/2) * np.sin(x*0.35*2*np.pi), np.exp(-x*x/2) * np.sin(x*0.85*2*np.pi)]  

for i in range(5):
    plt.plot(x,(h[i]))


plt.show()
