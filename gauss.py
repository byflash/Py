import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

def gaussian(N,x):
    return (np.sqrt(N[1]*2*np.pi))**(-1)*np.exp(-(x-N[0])**2/(2*N[1]))#modifying

def errorfunc(N,x,z):
        return gaussian(N,x)-z

N = np.array([72.4, 9.0], dtype=np.float)
x = np.linspace(N[0]-3.0*np.sqrt(N[1]), N[0]+3.0*np.sqrt(N[1]), num=100, endpoint=True)
noise = np.random.randn(100) * 0.03
z = gaussian(N,x)
noisyz = z + noise

N0 = np.array([72.4, 9.0], dtype=np.float) #Initial guess
solp, ier = leastsq(errorfunc, 
                    N0, 
                    args=(x,noisyz),
                    Dfun=None,
                    full_output=False,
                    ftol=1e-9,
                    xtol=1e-9,
                    maxfev=100000,
                    epsfcn=1e-10,
                    factor=0.1)
y=gaussian(N,x)
plt.plot(x, z, 'r-', linewidth=1.5, alpha=0.6, label='Theoretical')
plt.scatter(x, noisyz, c='k', marker='+', color='k', label='Measured Data')
plt.plot(x, gaussian(solp,x), 'g--', linewidth=2, label='leastsq fit')
plt.xlim((N[0]-3*np.sqrt(N[1]), N[0]+3*np.sqrt(N[1])))
plt.ylim((0.0, np.sqrt(N[1]*2*np.pi)**(-1)+0.05))
plt.grid(which='major')

plt.show()