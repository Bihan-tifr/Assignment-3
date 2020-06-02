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

data=np.loadtxt("data2.txt")

k=data[:,0]
FT=data[:,1]

plt.title("prob2:Fourier transformation of sinc function")
plt.xlabel(r'$k\rightarrow$',fontsize=20)
plt.ylabel(r'$\tilde{f}\rightarrow$',fontsize=20)
plt.plot(k,FT,color='c',label = 'Numerical')
plt.plot(k,f(k),color='r',linestyle='dashed',label='Analytical')	
plt.legend()
plt.grid()
plt.savefig("p2.jpg")
plt.show()
