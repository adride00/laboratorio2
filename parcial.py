import csv
import codecs
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
archivo=codecs.open('borrowers_test.csv', encoding='utf-8')
ins=csv.reader(archivo,delimiter=',')

def shellSort(items):
    inc = len(items) / 2
    while inc:
        for i in xrange(len(items)):
            j = i
            temp = items[i]
            while j >= inc and items[j-inc] > temp:
                items[j] = items[j - inc]
                j -= inc
            items[j] = temp
        inc = inc/2 if inc/2 else (0 if inc==1 else 1)
listaApe=[]

for line in ins:
	apellidos=line[0].strip()
	listaApe.append(apellidos)

shellSort(listaApe)
for i in listaApe:
	print i
