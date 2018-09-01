import numpy as np
import matplotlib.pylab as plt

arch = np.genfromtxt("647_Global_Temperature_Data_File.txt")

years=arch[:,0]
T1=arch[:,1]
suav=arch[:,2]



#plt.plot(years, T1)
#plt.savefig("Grafica_temp.pdf")

years05=[]
for i in range(len(T1)):
	if T1[i]>0.5:
		years05.append(years[i])

####20 AÑOS MAS CALIENTES
dic_T={}	#Relaciona los anios y las anomalias de temperatura en un diccionario
for i in range(len(years)):
	dic_T[years[i]] = T1[i]
#print (dic_T)

dic_ord=sorted(dic_T.items(), key=lambda x: x[1]) #organiza los elementos del diccionario
total_items=len(dic_ord)
ult_20=dic_ord[total_items-20:total_items]
#print (ult_20) #Imprime los 20 ultimos - Es una lista

###Crea una lista con los 20 años más calientes
years_hot=[]
for l in ult_20:
	years_hot.append(l[0])
print (years_hot)
###Crea una lista con las 20 temps más calientes
T_hot=[]
for l in ult_20:
	T_hot.append(l[1])

plt.plot(years, suav, label='Suavizado')
plt.plot(years_hot, T_hot, 'ro', label='20 mas calientes')
plt.suptitle('Temperatura suavizada y 20 mas calientes vs. Año')
plt.legend()
plt.show()
