##Rectangulos
##ANDRES FELIPE LAVERDE MARTINEZ
class rectangulo:
	def __init__(self, x0, y0, lx_0, ly_0):
		self.x0=x0  #Punto del centro del rectangulo con coordenadas (x,y)
		self.y0=y0
		self.lx=lx_0 #Lados del rectangulo, horizontal inferior
		self.ly=ly_0 #vertical derecho

		#----->Los lados deben ser siempre positivos<-----#
		#vertice 1, inferior izquierdo
		self.x1=self.x0-(self.lx/2.0)
		self.y1=self.y0-(self.ly/2.0)
		#vertice 2, inferior derecho
		self.x2=self.x0+(self.lx/2.0)
		self.y2=self.y0-(self.ly/2.0)
		#vertice 3, superior izquierdo
		self.x3=self.x0-(self.lx/2.0)
		self.y3=self.y0+(self.ly/2.0)
		#vertice 4, superior derecho
		self.x4=self.x0+(self.lx/2.0)
		self.y4=self.y0+(self.ly/2.0)
		
		self.centro=[self.x0, self.y0]
		self.punto1=[self.x1, self.y1]
		self.punto2=[self.x2, self.y2]
		self.punto3=[self.x3, self.y3]
		self.punto4=[self.x4, self.y4]


		# Punto3--------------Punto4
		#   |         lx         |
		#  l|                    |
		#  y|       CENTRO       |
		#   |                    |
		#   |                    |
		# Punto1--------------Punto2		

	def dar_vertices(self):
		print (self.punto1, self.punto2, self.punto3, self.punto4)

rec1=rectangulo(3.0, 1.0, 2.0, 6.0)
rec2=rectangulo(2.5,2.0, 3.0, 2.0)
#rec1.dar_vertices()
#rec2.dar_vertices()

def interseccion(r1, r2):
	##################### NINGUNA ############################
	if r1.x4<r2.x1 or r2.x4<r1.x1 or r1.y4<r2.y1  or r2.y4<r1.y1: #No hay interseccion
		print ("Los rectangulos no se intersectan")

	##################### UN PUNTO ##########################	
	elif r1.punto4==r2.punto1:#Un punto tipo 1
		print ("los rectangulos se tocan en un solo punto de coordenadas",r1.punto4)
	elif r2.punto4==r1.punto1:#Un punto tipo 1 prima
		print ("los rectangulos se tocan en un solo punto de coordenadas",r2.punto4)
	elif r1.punto3==r2.punto2:#Un punto tipo 2
		print ("los rectangulos se tocan en un solo punto de coordenadas",r1.punto3)
	elif r2.punto3==r1.punto2:#Un punto tipo 2 prima
		print ("los rectangulos se tocan en un solo punto de coordenadas",r2.punto3)
	
	##################### EN CRUZ ############################
	elif r2.y4>r1.y4 and r2.y1<r1.y1 and r1.x1<r2.x1 and r1.x4>r2.x4:
		l_interx=r2.lx
		l_intery=r1.ly
		print ("los rectangulos se intersectan formando un rectangulo de lados", l_interx,",",l_intery)
	elif r1.y4>r2.y4 and r1.y1<r2.y1 and r2.x1<r1.x1 and r2.x4>r1.x4:
		l_interx=r1.lx
		l_intery=r2.ly
		print ("los rectangulos se intersectan formando un rectangulo de lados", l_interx,",",l_intery)

	############## UN RECTANGULO EN LAS ESQUINAS ################
	elif r1.x4>r2.x1 and r1.x1<r2.x1 and r2.x4>r1.x4 and r1.y4>r2.y1 and r1.y1<r2.y1 and r2.y4>r1.y4: #Un rectangulo en la esquina tipo 1
		l_interx=r1.x4-r2.x1  #Lados de la interseccion
		l_intery=r1.y4-r2.y1
		print ("los rectangulos se intersectan formando un rectangulo de lados", l_interx, ",", l_intery)
	elif r2.x4>r1.x1 and r2.x1<r1.x1 and r1.x4>r2.x4 and r2.y4>r1.y1 and r2.y1<r1.y1 and r1.y4>r2.y4: #Un rectangulo en la esquina tipo 1 prima
		l_interx=r2.x4-r1.x1
		l_intery=r2.y4-r1.y1
		print ("los rectangulos se intersectan formando un rectangulo de lados", l_interx, ",", l_intery)
	elif r1.x4>r2.x4 and r1.x1<r2.x4 and r1.x1>r2.x1 and r1.y4<r2.y4 and r1.y4>r2.y1 and r1.y1<r2.y1: #Un retangulo en la esquina tipo 2
		l_interx=r2.x4-r1.x1
		l_intery=r1.y4-r2.y1
		print ("los rectangulos se intersectan formando un rectangulo de lados", l_interx, ",", l_intery)
	elif r2.x4>r1.x4 and r2.x1<r1.x4 and r2.x1>r1.x1 and r2.y4<r1.y4 and r2.y4>r1.y1 and r2.y1<r1.y1: #Un retangulo en la esquina tipo 2 prima
		l_interx=r1.x4-r2.x1
		l_intery=r2.y4-r1.y1
		print ("los rectangulos se intersectan formando un rectangulo de lados", l_interx, ",", l_intery)

	################### RECTANGULO ADENTRO #######################
	elif r1.x1<=r2.x1 and r1.y1<=r2.y1 and r1.x2>=r2.x2 and r1.y4>=r2.y4:
		print ("Los rectangulos se intersectan formando un rectangulo de lados", float(r2.lx), ",", float(r2.ly))
	elif r2.x1<=r1.x1 and r2.y1<=r2.y1 and r2.x2>=r1.x2 and r2.y4>=r1.y4:
		print ("Los rectangulos se intersectan formando un rectangulo de lados", float(r1.lx), ",", float(r1.ly))

	################## POR UN LADO ###############################
	elif r1.y1<r2.y1 and r1.y4>r2.y4 and r1.x1<r2.x4 and r1.x1>r2.x1:#Lado izquierdo 
		l_interx=r2.x4-r1.x1
		print ("Los rectangulos se intersectan formando un rectangulo de lados", l_interx,",",float(r2.ly))
	elif r2.y1<r1.y1 and r2.y4>r1.y4 and r2.x1<r1.x4 and r2.x1>r1.x1:#Lado izquierdo prima
		l_interx=r1.x4-r2.x1
		print ("Los rectangulos se intersectan formando un rectangulo de lados", l_interx,",",float(r1.ly))
	elif r1.y1<r2.y1 and r1.y4>r2.y4 and r2.x4>r1.x4 and r2.x1<r1.x4:#Lado derecho
		l_interx=r1.x4-r2.x1
		print ("Los rectangulos se intersectan formando un rectangulo de lados", l_interx,",",float(r2.ly))
	elif r2.y1<r1.y1 and r2.y4>r1.y4 and r1.x4>r2.x4 and r1.x1<r2.x4:#Lado derecho prima
		l_interx=r2.x4-r1.x1
		print ("Los rectangulos se intersectan formando un rectangulo de lados", l_interx,",",float(r1.ly))

	############### POR ARRIBA O ABAJO ###############################
	elif r1.x1<=r2.x1 and r1.x4>=r2.x4 and r1.y4>r2.y1 and r1.y4<r2.y4:#Arriba
		l_intery=r1.y4-r2.y1
		print ("Los rectangulos se intersectan formando un rectangulo de lados", float(r2.lx),",",l_intery)
	elif r2.x1<=r1.x1 and r2.x4>=r1.x4 and r2.y4>r1.y1 and r2.y4<r1.y4:#Arriba prima
		l_intery=r2.y4-r1.y1
		print ("Los rectangulos se intersectan formando un rectangulo de lados", float(r1.lx),",",l_intery)
	elif r1.x1<=r2.x1 and r1.x4>=r2.x4 and r1.y1<r2.y4 and r1.y1>r2.y1:#Abajo
		l_intery=r2.y4-r1.y1
		print ("Los rectangulos se intersectan formando un rectangulo de lados", float(r2.lx),",",l_intery)
	elif r2.x1<=r1.x1 and r2.x4<=r1.x4 and r2.y1<r1.y4 and r2.y1>r1.y1:#Abajo prima
		l_intery=r1.y4-r2.y1
		print ("Los rectangulos se intersectan formando un rectangulo de lados", float(r1.lx),",",l_intery)

	################## POR UNA LINEA ###########################
	elif r1.x1==r2.x4 or r1.x4==r2.x1 or r1.y1==r2.y4 or r1.y4==r2.y1:
		print ("Los rectangulos se intersectan en una linea")

interseccion(rec1, rec2)
##ANDRES FELIPE LAVERDE MARTINEZ
