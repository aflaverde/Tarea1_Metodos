##Integrales
import numpy as np
import matplotlib.pyplot as plt
import random
import math

pi=np.pi

def f1(x):
	y = np.cos(x)
	return y
a=-pi/2.
b=pi
N=10001
x1 = np.linspace(-pi/2., pi, N)

#Analitica
valor_analitica=np.sin(pi)-np.sin(-pi/2)


#Trapezoide------------------------------------
def integral_trap(f, x):
	total=0.0
	h=x[1]-x[0]
	#h = (x[N-1]-x[0])/(N)
	for i in range(len(x)):
		total+=h*(f1(x[i])+f1(x[i-1]))/2.0
	return total

#Simpson---------------------------------------
def integral_sim(f, a, b, n):
	h=(b-a)/n
	suma=0.0
	i=0.0
	while i<=b:
		if i+h<=b:
			suma+=(h/6.0)*(f(i)+(13./4.1)*f((i+h)/2.0)+f(i+h))
		i+=h
	return suma

#Montecarlo------------------------------------
def integral_MC(f, min_x, max_x, x, n):
	min_y=min(f(x))
	max_y=max(f(x))	
	random_x1=np.random.random(n)*(max_x-min_x)+min_x
	random_y1=np.random.random(n)*(max_y-min_y)+min_y
	h=f(random_x1)-random_y1
	i=0.0
	area=0.0
	if h[0]>0.0:
		debajo=np.where(h>0.0)
		total=float(len(debajo))
		area+=(max_y-min_y)*(max_x-min_x)
		integral=area*(total/(1.0*float(len(random_y1))))
	elif h[0]<0.0:
		encima=np.where(h<0.0)
		total2=float(len(encima))
		area+=-1.0*(max_y-min_y)*(max_x-min_x)
		integral=area*(total2/(1.0*float(len(random_y1))))
	return integral
	return type(h)
print ("tipo",integral_MC(f1, a, b, x1, N))

#Valores medios--------------------------------
def integral_VM(f, a, b, n):
	random_x=np.random.random(n)*(b-a)+a
	y=f1(random_x)
	prom=np.mean(y)
	integral=prom*(b-a)
	return integral

#Error.....
def error(f, a, b, x, metodo, n):
	if metodo=="Trapezoides" or metodo=="trapezoides":
		err = (integral_trap(f, x) - valor_analitica)/valor_analitica
        
	elif metodo=="Simpson" or metodo=="simpson":
       		err = (integral_sim(f, a, b, n) - valor_analitica)/valor_analitica

	elif metodo=="vm" or metodo=="VM":
		err = (integral_VM(f, a, b, n) - valor_analitica)/valor_analitica

	elif metodo=="MC" or metodo=="mc" or metodo=="Monte Carlo" or metodo=="monte carlo":
		err = (integral_MC(f, a, b, x, n) - valor_analitica)/valor_analitica
	return (abs(err))

#Impresion---------------------------------------------------------
print ("Trapezoides ", integral_trap(f1, x1), "Error=", error(f1, a, b, x1, "trapezoides", N))
print ("SIMPSON", integral_sim(f1, a, b, N), "Error=", error(f1, a, b, x1, "Simpson", N))
print ("Monte carlo", integral_MC(f1, a, b, x1, N), "Error=", error(f1, a, b, x1, "mc", N))
print ("Valores medios ", integral_VM(f1, a, b, N), "Error=",error(f1, a, b, x1, "vm", N))

