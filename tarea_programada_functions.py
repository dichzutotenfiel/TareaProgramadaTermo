import numpy as np
import matplotlib.pyplot as plt
from math import log
from collections import Counter


def posiciones_iniciales(plano): 

	#in: plano(np.array)
	#out: plano(np.array)
	#descrp: itera sobre la matriz "plano" y genera las posiciones 
	#iniciales con valores 1 en el centro
	
	size = np.shape(plano)[1]
	for i in range(size):
		for j in range(size):
			if  (size/2)-5 < i <= (size/2)+5 and (size/2)-5 < j <= (size/2)+5:
				plano[i][j] = 1
	return plano

def von_neighbours(grid, row, col):

	#in: grid(np.array)
	#out: a(list)
	#descrp: se itera sobre la matriz para determinar los posibles
	#vecinos de von neumann, devuelve una lista con las 
	#posibles coordenadas de movimiento
	#


	a = []
	for x, y in ((row - 1, col), (row + 1, col), (row, col - 1),
			(row, col + 1)):
		if not (0 <= x < len(grid) and 0 <= y < len(grid[x])):
			continue
		if grid[x][y] == 0:
			a.append((x,y))
	return a


def posiciones(plano):

	#in: plano(np.array)
	#out: [datax,datay](list)
	#descrp: se itera para encontrar las posiciones de las particulas
	#

	datax = []
	datay = [] 
	for i in range(np.shape(plano)[1]):
		for j in range(np.shape(plano)[1]):
			if plano[i][j] == 1:
				datax.append([i])
				datay.append([j])
	return([datax,datay])



def entropia(lista):

	#in: lista(list)
	#out: total(float)
	#descrp: Calcula la entropia de Shannon para una lista de probabilidad
	#dada

	total = 0

	for valor in lista:
		if valor == 0.0:
			continue
		total += valor*log(valor)

	if total != 0:
		total *= -1

	return total


