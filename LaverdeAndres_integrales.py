##Integrales
import numpy as np
import matplotlib.pyplot as plt
pi=np.pi

def f1(x):
	y = np.cos(x)
	return y

N=10001
x1 = np.linspace(-pi/2., pi, N)

#Analitica
def analitica(x):
	y = -np.sin(x)
	return y

#Trapezoide
def integral_trap(f, x):
	total = 0.0
	h = x[1]-x[0]
	#h = (x[N-1]-x[0])/(N)
	for i in range(len(x)):
		total += h*(f1(x[i])+f1(x[i-1]))/2.0
	return total

#Error
def error(f, x, metodo):
	if metodo=="Trapezoides" or metodo=="trapezoides":
		err = (integral_trap(f, x) - analitica(x))/analitica(x)
	return err 

print "Trapezoides ", integral_trap(f1, x1), "Error=", error(f1, x1, "trapezoides")
