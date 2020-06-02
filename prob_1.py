import numpy as np
import matplotlib.pyplot as plt
def f(x):#Definition of the sinc function
	if x !=0:
		y=(1/x)*np.sin(x)
	else:
		y=1
	return y
def fk(x):
	if abs(x)<=1:						#Analytical result of Fourier Transform
		y=np.sqrt((np.pi)/2)
	else:
		y=0
	return y
N=250
x_min=-50
x_max=50
x=np.linspace(x_min,x_max,N)
delta = (x_max-x_min)/(N-1)
fx,fk_exact=[],[]

for i in range(N):
	fx.append(f(x[i]))

n_fft = np.fft.fft(fx, norm='ortho') 			#computing dft
k = np.fft.fftfreq(N, d=delta)
k = 2*np.pi*k
factor = np.exp(-1j * k * x_min)

FT = delta * np.sqrt(N/(2.0*np.pi)) * factor * n_fft 		#Computing fourier transform numerically

for i in range(k.size):
	fk_exact.append(fk(k[i]))	#exact result
	
plt.title("Fourier transformation of sinc function")
plt.plot(k,FT,color='c',label = 'Numerical')
plt.plot(k,fk_exact,color='r',label='Analytical')
plt.xlabel(r'$k\rightarrow$',fontsize=20)
plt.ylabel(r'$\tilde{f}\rightarrow$',fontsize=20)
	
plt.legend()
plt.grid()
plt.savefig("p1.jpg")
plt.show()
