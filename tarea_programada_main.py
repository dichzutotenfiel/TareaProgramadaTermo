import numpy as np
import matplotlib.pyplot as plt
from tarea_programada_functions import *
import pylab
from collections import Counter

#--------------inicializacion de posiciones---------------

N = 100
plano_cafe = np.zeros((N,N))
pasos = 20000
plano_cafe = posiciones_iniciales(plano_cafe)


#--------------Movimiento de particulas-------------------
matrices = open("matrices.txt","a+")
entrop = []
step = []
sum_lineas = np.zeros((100,1))
for k in range(pasos):
	for i in range(0,N):
		for j in range(0,N):
			if plano_cafe[i][j] == 1:
				a = von_neighbours(plano_cafe,i,j)
				if not a:
					continue
				else:       
					choice = np.random.choice(a=range(len(a)), replace=True)
					coords = a[choice]
					plano_cafe[coords[0]][coords[1]] = 1
					plano_cafe[i][j] = 0 

	#---------------Calculo de probabilidades------------
	for linea in range(len(plano_cafe)):
		sum_lineas[linea] += plano_cafe[linea].sum()
	proba = sum_lineas/((k+1)*100)
	entrop.append(entropia(proba))
	step.append(k)

	#---------GRAFICAS DE 0 10 100 1000 10000------------
	values = [0, 10 , 100, 1000, 10000]
	for i in values:
		if k == i:
			dx, dy = posiciones(plano_cafe)
			plt.xlim(0, N)
			plt.ylim(0, N)
			plt.scatter(dx,dy)
			# Don't mess with the limits!
			plt.autoscale(False)
			plt.title("Paso "+str(k))
			plt.ylabel("Y")
			plt.xlabel("X")
			plt.savefig("Paso"+str(k)+".png") 
			plt.close()

	#---------Guardar Matrices---------------------------
	matrices.write("Paso" + str(k)+"\n")
	for line in plano_cafe: 
		matrices.write(str(line)+"\n")
	matrices.write("\n\n\n")

#------Graficacion de entropia y ultimo estado-----------


matrices.close()
plt.plot(step,entrop)
plt.title("Entropia vs Pasos")
plt.ylabel("Entropia")
plt.xlabel("Pasos")
plt.savefig("entropia.png")
plt.close()