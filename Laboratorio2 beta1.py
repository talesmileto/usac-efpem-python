# Laboratorio 2
# Programacion Comercial II

# Autor:
# Jorge Luis Perez Canto
# Carnet: 201024865

archivo=open('departamentos.txt')
diccionario = dict()

for linea in archivo:
    palabra = linea.strip()
    palabras = linea.split()
    diccionario[palabras[0]] = palabras[1]

print "\nEl diccionario formado: \n"
print diccionario

import random
depto = diccionario.keys()
print "Al azar: \n"

Correcto=0
Incorrecto=0

while True:
    palabra =  random.choice(depto)
    print "¿Nombre de la cabezera de", palabra, "? (Escriba 'fin' para salir)"
    cabezera=raw_input()
    
    if cabezera.lower()==diccionario[palabra].lower():
        print "Respuesta Correcta\n"
        Correcto=Correcto+1
    else:
        if cabezera.lower()=="fin":
            print "Saliendo...\n"
            break
        else:
            print "Respuesta Incorrecta"
            print "La respuesta correcta es:", diccionario[palabra]
            Incorrecto=Incorrecto+1
            print "\n"

print "Total de respuestas correctas:", Correcto
print "Total de respuestas incorrectas:", Incorrecto

if Correcto>Incorrecto:
    print "Felicidades..."
