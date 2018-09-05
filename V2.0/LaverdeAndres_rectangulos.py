##Rectangulos
class rectangulo:
	def __init__(self, x0, y0, lx_0, ly_0):
		self.x1=x0  #Punto de un solo vertice 1 inicial con coordenadas (x,y)
		self.y1=y0
		self.lx=abs(lx_0) #Lados del rectangulo, horizontal inferior
		self.ly=abs(ly_0) #vertical derecho

		#----->Los lados deben ser siempre positivos<-----#

		#vertice 2, en la horizontal
		self.x2=self.x1+self.lx
		self.y2=self.y1
		#vertice 3, en la vertical
		self.x3=self.x1
		self.y3=self.y1+self.ly
		#vertice 4, en la horizontal
		self.x4=self.x1+self.lx
		self.y4=self.y1+self.ly

		# Punto3--------------Punto4
		#   |         lx         |
		#  l|                    |
		#  y|       FORMA        |
		#   |                    |
		#   |                    |
		# Punto1--------------Punto2

		self.punto1=[self.x1, self.y1]
		self.punto2=[self.x2, self.y2]
		self.punto3=[self.x3, self.y3]
		self.punto4=[self.x4, self.y4]

	def dar_vertices(self):
		print (self.punto1, self.punto2, self.punto3, self.punto4)

rec1=rectangulo(1, 1, 3, 2)
rec2=rectangulo(3, 2, 3, 3)
rec1.dar_vertices()
rec2.dar_vertices()

def interseccion(r1, r2):
	if r1.x4<r2.x1 or r2.x4<r1.x1 or r1.y4<r2.y1  or r2.y4<r1.y1: #No hay interseccion
		print "Los rectangulos no se intersectan"
	elif r1.punto4==r2.punto1 or r2.punto4==r1.punto1: #Un punto tipo 1
		print "los rectangulos se tocan en un solo punto de coordenadas",r1.punto4
	elif r1.punto3==r2.punto2 or r2.punto3==r1.punto2: #Un punto tipo 2
		print "los rectangulos se tocan en un solo punto de coordenadas",r1.punto3
	####################################################################
	elif r1.x4>r2.x1 and r1.x1<r2.x1 and r2.x4>r1.x4 and r1.y4>r2.y1 and r1.y1<r2.y1 and r2.y4>r1.y4:
		l_interx=r1.x4-r2.x1  #Lados de la interseccion
		l_intery=r1.y4-r2.y1
		print "los rectangulos se intersectan formandi un rectangulo de lados", l_interx, "y", l_intery
interseccion(rec1, rec2)



