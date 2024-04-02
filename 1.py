import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(-x*x/2) * np.sin(x*0.99*2*np.pi)
x = np.linspace(0, 100, 500)
y = f(x)
plt.plot(x, y, label='y = s')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de y = sin(x)')

plt.legend()

plt.show()
