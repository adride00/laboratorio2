import numpy as np
import matplotlib.pyplot as plt
import csv
import codecs
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
archivo=open('borrowers_test.csv')
ins=csv.reader(archivo,delimiter=',')
#sys.setrecursionlimit(10)
def burbuja(lista,tam):
    for i in range(1,tam):
        for j in range(0,tam-i):
            if(lista[j] > lista[j+1]):
                k = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = k;
 
def imprimeLista(lista,tam):
    for i in range(0,tam):
        print apellidos[i]
        
def buscarc(carrer):
	cont=0
	archivo=open('borrowers_test.csv')
	ins=csv.reader(archivo,delimiter=',')
	for line in ins:
		car=line[6]
		if codecs.decode(car,'utf-8')==carrer:
			cont+=1
	return cont		
def busqueda_secuencial(nombre):
	archivo=open('borrowers_test.csv')
	ins=csv.reader(archivo,delimiter=',')
	allnom=[]
	posicion=0
	encontrado=False
	posicion_valor_buscar=[]
	for line in ins:
		nombre=line[1]
		nom=nombre.split(" ")
		posicion+=1
		if nombre.upper() in nom or nombre.capitalize() in nom:
			print posicion
			print line
			
def buscar(nombres,bus):
	numNom=0
	archivo=open('borrowers_test.csv')
	ins=csv.reader(archivo,delimiter=',')
	listaApe=[]
	listaNom=[]
	for line in ins:
		nombre=line[bus]
		nom=nombre.split(' ')
		if nombres.upper() in nom or nombres.capitalize() in nom:
			print nom
			numNom +=1
	return numNom
while True:
	print "--------------------------------MENU-----------------------------------"
	print "1) cantidad de hombres y mujeres"
	print "2) Hacer busqueda por nombres o apellidos"
	print "3) Mostrar cantidad de estudiantes agrupados por carreras"
	print "4) Mostrar cantidad de datos erroneos (NULL, Espacios,otros)"
	print "5) Agfregar registros"
	print "6) Ordenar registros por orden alfabetico"
	print "7) Utilizar quicksort"
	print "8) Graficar datos"
	print "9) Salir"
	print "\n Ingrese opcion"
	opc=int(raw_input(">>>"))
	if opc==1:
		UserM=0
		UserF=0
		for line in ins:
			genero=line[4]
			if genero=='F':
				UserF+=1
			if genero=='M':
				UserM+=1
		print 'Cantidad del sexo masculino '
		print UserM
		print 'Cantidad del sexo femenino '
		print UserF	
	if opc==2:
		print "--------ELEGIR ALGORITMO-----------"
		print " 1) Algortimo lineal"
		print " 2) Algoritmo secuencial"
		print " 3) Algoritmo binario"
		algo=int(raw_input(">>>"))
		if algo==1:
			print "1) Buscar por nombres"
			print "2) Buscar por apellidos"
			opc=int(raw_input(">>>"))
			if opc==1:
				nom=raw_input("Nombre: >>>")
				print buscar(nom,1)
			if opc==2:
				nom=raw_input("Nombre: >>>")
				print buscar(nom,0)
		if algo==2:
			busqueda_secuencial("adrian")
	if opc==3:
		listCarrera=[]
		lista=[]
		archivo=open('borrowers_test.csv')
		ins=csv.reader(archivo,delimiter=',')
		for line in ins:
			carrera=line[6].strip()
			listCarrera.append(carrera)
		lista=list(set(listCarrera))
		lista.pop(0)
		lista.pop(15)
		lista.pop(19)
		lista.pop(38)
		print 'Total de carreras: ', len(lista)
		#for i in range(len(lista)):
		#	var=codecs.decode(lista[i],'utf-8')
			#print var
		for y in range(len(lista)):
			print codecs.decode(lista[y],'utf-8')
			print buscarc(codecs.decode(lista[y],'utf-8'))
	if opc==4:
		listanull=[]
		listavacios=[]
		for file in ins:
			nu=file[1]
			vacio=[5]
			if nu =='NULL':
				listanull.append(nu)
			if vacio=="":
				listavacios.append(vacio)
				
					
		print 'Total de datos erroneos (nulos y vacios) ',len(listanull)+len(listavacios)
	if opc==5:
		continue
	if opc==6:
		print "-----------Algoritmos de ordenamiento----------"
		print "1) Algoritmo de la burbuja"
		print "2) Algoritmo Quicksort"
		algoritmo=int(raw_input(" Elija opcion >>>"))
		if algoritmo==1:
			archivo=codecs.open('borrowers_test.csv', encoding='utf-8')
			ins=csv.reader(archivo,delimiter=',')
			apellidos=[]
			for line in ins:
				apellido=line[0].strip()
				apellidos.append(apellido)
			#for i in range(len(apellidos)):	
			#	print codecs.decode(apellidos[i],'utf-8')

			burbuja(apellidos,len(apellidos))
			imprimeLista(apellidos,len(apellidos))
		if algoritmo==2:
			archivo=codecs.open('borrowers_test.csv', encoding='utf-8')
			ins=csv.reader(archivo,delimiter=',')
			def quicksort(lista,izq,der):
				i=izq
				j=der
				x=lista[(izq + der)/2]
			 
				while( i <= j ):
					while lista[i]<x and j<=der:
						i=i+1
					while x<lista[j] and j>izq:
						j=j-1
					if i<=j:
						aux = lista[i]; lista[i] = lista[j]; lista[j] = aux;
						i=i+1;  j=j-1;
			 
					if izq < j:
						quicksort(lista, izq, j);
				if i < der:
					quicksort( lista, i, der );
			 
			def imprimeLista(lista,tam):
				for i in range(0,tam):
					print lista[i]

			listaape=[]
			for line in ins:
				apellido=line[0].strip()
				
				if apellido is not 'NULL' and len(apellido.split(' ')) < 3:
					listaape.append(apellido)
			for i in listaape:
				print i		
			quicksort(listaape,0,len(listaape)-1)
			imprimeLista(listaape,len(listaape))
	if opc==8:
		archivo=open('borrowers_test.csv')
		ins=csv.reader(archivo,delimiter=',')
		UserM=0
		UserF=0
		for line in ins:
			genero=line[4]
			if genero=='F':
				UserF+=1
			if genero=='M':
				UserM+=1
		print 'Cantidad del sexo masculino '
		print UserM
		print 'Cantidad del sexo femenino '
		print UserF	
		
		N = 2
		print "\n","Preparando estadisticas......" , "\n"		
		menMeans = (UserM,UserF) 
		menStd =  (8)
		ind = np.arange(N)  
		width = 0.35       
		fig, ax = plt.subplots()
		rects1 = ax.bar(ind, menMeans, width, color='g', yerr=menStd)

		ax.set_ylabel('Resultados')
		ax.set_title('Hombres vs Mujeres')
		ax.set_xticks(ind + width)
		ax.set_xticklabels(('Hombres', 'Mujeres'))
				
		def autolabel(rects):
			for rect in rects:
				height = rect.get_height()
				ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
						'%d' % int(height),
						ha='center', va='bottom')
		autolabel(rects1)
		plt.show()
	if opc==9:
		break			
						
					
