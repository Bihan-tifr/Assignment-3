import numpy as np 
import matplotlib.pyplot as plt 

w=np.loadtxt("noise.txt")
N=len(w)
nft=np.fft.fft(w,norm='ortho')
k= 2*np.pi*np.fft.fftfreq(N, d=1)
power_spec,x=[],[]
for i in range(N):
	x.append(i)
	k1=(1/N)*(np.absolute(w[i]))**2
	power_spec.append(k1)
###Plotting#############
bins = 20
fig=plt.figure()
plt.subplot(2,2,1)
plt.plot(x,w,'blue')
plt.xlabel(r't',fontsize=15)
plt.ylabel(r'f',fontsize=15)
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(k,nft,'green')
plt.xlabel(r'$\omega$',fontsize=16)
plt.ylabel(r'$f(\omega)$',fontsize=16)

plt.grid(True)

plt.subplot(2,2,3)
plt.plot(k,power_spec,'cyan')

plt.xlabel(r'$\omega$',fontsize=16)
plt.ylabel(r'$|f(\omega)|^2$',fontsize=16)
plt.grid(True)

plt.subplot(2,2,4)
plt.hist(power_spec,bins, facecolor='red')
plt.xlabel(r'$\omega$',fontsize=16)
plt.ylabel(r'$|f(\omega_{binned})|^2$',fontsize=16)

plt.grid(True)
plt.show()
