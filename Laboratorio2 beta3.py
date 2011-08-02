# USAC/EFPEM/CI

# Laboratorio 2
# Programacion Comercial II

# Descripcion:
# Este programa realiza un examen sobre lo nombres de las cabezeras de los departamentos
# de la Republica de Guatemala.

# Autor:
# Jorge Luis Perez Canto
# Carnet: 201024865


archivo=open('departamentos.txt') #Se abre el archivo que contiene el listado de nombres de departamentos y sus cabezeras
diccionario = dict()

for linea in archivo:
    palabra = linea.strip()
    palabra = palabra.split("  ") # Se define dos espacios en blanco como separador entre el nombre del departamento y el de la cabezera.
    diccionario[palabra[0]] = palabra[1] # Se va creando el diccionario.

print "\nEl diccionario formado: \n"
print "\n", diccionario, "\n"

Correcto=0
Incorrecto=0

while True:
    import random
    depto = diccionario.keys()
    
    try:
        departamento = random.choice(depto) # Se genera una nombre de departamento alazar
        print "\nNombre de la cabezera de", departamento, "? (Escriba 'fin' para salir)"
        cabezera=raw_input()

        # Se verifica si el nombre de la cabezera corresponde al departamento correspondiente
        if cabezera.lower()==diccionario[departamento].lower():
            print "Respuesta Correcta.\n"
            Correcto=Correcto+1

        else:
            if cabezera.lower()=="fin": #Si se escribe la palabra fin, se termina el ciclo.
                break
            else:
                print "Respuesta Incorrecta. La respuesta correcta era:", diccionario[departamento]
                Incorrecto=Incorrecto+1
                print ""
        del diccionario[departamento]
    except:
        break

# Se muestra la cantidad de aciertos y fallas:  
print "\nTotal de respuestas correctas:", Correcto
print "Total de respuestas incorrectas:", Incorrecto

if Correcto>Incorrecto:
    print "\nFelicidades..."
