# Laboratorio no. 1
# Programacion Cientifica II

#DESCRIPPCION:
# Este programa guarda los numeros telefonicos de sus amigos y luego permite realizar una llamada.


#AUTOR:

# Jorge Luis Perez Canto
# 201024865


nombres=[]
numeros=[]

while True:
    try:
        cantidad=int(raw_input('Ingrese la cantidad de amigos que desea guardar en su lista de contactos:\n'))
    except:
        print '\nPor favor ingrese solo numeros enteros, \n(presione la tecla ENTER para volver a intentarlo).'
        raw_input()        
    else:
        def Agregar(nombres, numeros):
            for x in range(cantidad):
                Nombre=raw_input('\n\nIngrese el nombre de su amigo\n')
                nombres.append(Nombre)
                while True:
                    try:
                        print 'Ingrese el numero telefonico de', Nombre
                        Numero=int(raw_input())
                    except:
                        print '\nPor favor ingrese solo numeros enteros \n(Presione la tecla ENTER para volver a intentarlo).'
                        raw_input()
                    else:
                        numeros.append(Numero)
                        break
        break
    
def Llamar(nombres, numeros):
    salir = False
    while True:
        print '\n\nSi desea realizar una llamada presione la tecla Enter, \n(Escriba Fin para salir)'
        y=raw_input()
        if y.upper()=='FIN':
            break
        else:
            while not salir:
                NombreTemp=raw_input('\nIngrese el nombre de su amigo a llamar: ')
                if NombreTemp in nombres:
                    pos=nombres.index(NombreTemp)
                    print '\nLlamando al numero: ', numeros[pos]
                else:
                    print '\nError, no tengo el numero'

                entrada=raw_input('\nPara realizar otra llamada presione la tecla Enter, \n(escriba Fin para salir)\n ')
                if entrada.upper()=='FIN':
                    salir = True
            break

Agregar(nombres, numeros)
Llamar(nombres, numeros)
