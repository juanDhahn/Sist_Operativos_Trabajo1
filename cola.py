from collections import Counter

def crearCola():
	lista = []
	return lista

def agregar(cola, valor):
	cola.append(valor)

def conexionRestablecida(cola):
	#enviar al servidor
	#Estado normal
	if len(cola) <= 1:
		#Enviar el archivo
		cola = []
		return
	#revision estado lleno
	diccionario = Counter(cola)
	for valores in diccionario:
		if diccionario[valores]==1:
			#enviar
		else:
			#preguntar
			#try entre "yes" y "no"
			#if "yes"
			#if "no"
	cola=[]
