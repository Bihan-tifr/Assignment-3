import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.exp(-x**2)
def Fk(k):
	return np.exp(-k**2/4)/np.sqrt(2)

data=np.loadtxt("data4.txt")

k=data[:,0]
FT=data[:,1]
x=np.linspace(-5,5,100)

fig, ax= plt.subplots(1,2)
fig.suptitle("prob4:Fourier transform of gaussian using fftw")
ax[0].set_xlabel(r'$x\rightarrow$')
ax[0].set_ylabel(r'$f(x)\rightarrow$')
ax[0].set_title("Original function")
ax[0].plot(x,f(x),label=r'$e^{-x^2}$')
ax[0].grid(True)
ax[0].legend()

ax[1].set_xlabel(r'$k\rightarrow$')
ax[1].set_ylabel(r'$\tilde{f}(k)\rightarrow$')
ax[1].set_title("Fourier transformed function")
ax[1].plot(k,FT,'k',label="Numerical")
ax[1].plot(k,Fk(k),'y',linestyle="dashed",label=r'$\dfrac{e^{-k^2/4}}{\sqrt{2}}$ (Analytical)')
plt.grid(True)
plt.legend()
plt.savefig("p4.jpg")
plt.show()
