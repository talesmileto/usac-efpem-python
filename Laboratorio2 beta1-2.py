# -*- coding: cp1252 -*-
# Laboratorio 2
# Programacion Comercial II

# Autor:
# Jorge Luis Perez Canto
# Carnet: 201024865

archivo=open('depto.txt')
dic = dict()

for linea in archivo:
    palabra = linea.strip()
    palabras = linea.split()
    dic[palabras[0]] = palabras[1]

import random
de = dic.keys()

co=0
inc=0

while True:
    palabra =  random.choice(de)
    print "¿Nombre de la cabezera de", palabra, "? (Escriba 'fin' para salir)"
    ca=raw_input()
    
    if ca.lower()==dic[palabra].lower():
        print "Respuesta Correcta\n"
        co=co+1
    else:
        if ca.lower()=="fin":
            break
        else:
            print "Respuesta Incorrecta"
            print "La respuesta correcta es:", dic[palabra]
            inc=inc+1

print "Total de respuestas correctas:", co
print "Total de respuestas incorrectas:", inc

print "\ncode by george\n"

if co>inc:
    print "Felicidades..."
