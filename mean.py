﻿import numpy as np
import matplotlib.pyplot as plt

x = [4.6, 6.0, 2.0, 5.8]
sigma = [2.0, 1.5, 5.0, 1.0]

def gauss(x, mu, sigma):
    amp = 1 / (sigma * np.sqrt(2 * np.pi))
    exp = np.exp(-(x - mu)**2 / (2 * sigma**2))
    gauss = amp * exp
    return gauss

mu = np.linspace(0, 10, 1000)
c = 0
pro = np.zeros(len(mu))
for i in mu:
    Px = np.zeros(4)
    for i2 in range(4):
        Px[i2] = np.log(gauss(x[i2], i, sigma[i2]))
    pro[c] = np.sum(Px)
    c = c + 1

def maximo_sigma(x, y):
    deltax = x[1] - x[0]
    ii = np.argmax(y)
    d = (y[ii+1] - 2*y[ii] + y[ii-1]) / (deltax**2)
    return x[ii], 1/np.sqrt(-d)

prob = np.exp(pro)
prob = prob / sum(prob) * (1000/10)
plt.plot(mu, prob)
plt.xlabel(r'$\mu$')
plt.ylabel(r'$Post$')
plt.title(r'$\mu = $ %0.4f' %maximo_sigma(mu, pro)[0] + r'$\pm$ %0.4f' %maximo_sigma(mu, pro)[1])
plt.savefig('mean.png')
plt.show()