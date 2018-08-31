import numpy as np
import matplotlib.pylab as plt

arch = np.genfromtxt("647_Global_Temperature_Data_File.txt")

years=arch[:,0]
T1=arch[:,1]
suav=arch[:,2]
#print years, T1, suav

plt.plot(years, T1)
plt.savefig("Grafica_temp.pdf")
plt.axis('scaled')

years05=[]
for i in range(len(T1)):
	if T1[i]>0.5:
		years05.append(years[i])
#print years05

t_hot=[]	
years_hot=[]
for i in range(len(T1)):
	if T1[i]>T1[i-1]:
		t_hot.append(T1[i])
		years_hot.append(years[i])
print years_hot
print t_hot
#t_ord=sorted(T1)
#print t_ord


