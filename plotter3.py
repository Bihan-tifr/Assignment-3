import numpy as np
import matplotlib.pyplot as plt

def f(k):
	yl=[]
	for i in range(len(k)):
		s=k[i]
		if abs(s)<=1:
			y=np.sqrt((np.pi)/2)
		else:
			y=0
		yl.append(y)
	return yl

data=np.loadtxt("data3.txt")

k=data[:,0]
FT=data[:,1]


plt.xlabel(r'$k\rightarrow$',fontsize=18)
plt.ylabel(r'$\tilde{f}(k)\rightarrow$',fontsize=18)
plt.title("prob3: Fourier transformation of sinc function using gsl")
plt.plot(k,FT,label="Numerical")
plt.plot(k,f(k),'y',linestyle="dashed",label="Analytical")
plt.grid(True)
plt.legend()
plt.show()
