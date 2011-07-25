# Laboratorio no. 1
# Programacion Cientifica II

#DESCRIPPCION:
# Este programa guarda los num telefonicos de sus amigos y luego permite realizar una llamada.


#AUTOR:

# Jorge Luis Perez Canto
# 201024865


nom=[]
num=[]

while True:
    try:
        cant=int(raw_input('Cantidad de contactos:\n'))
    except:
        print '\nIngrese numeros.'
        raw_input()        
    else:
        def Add(nom, num):
            for x in range(cant):
                Nomb=raw_input('\n\nIngrese nombre ')
                nom.append(Nomb)
                while True:
                    try:
                        print 'Ingrese telefonico '
                        Numero=int(raw_input())
                    except:
                        print '\nIngrese solo numeros'
                        raw_input()
                    else:
                        num.append(Numero)
                        break
        break
    
def llamada(nom, num):
    salir = False
    while True:
        print '\n\nPara realizar una llamada presione la tecla Enter, \nFin para salir'
        y=raw_input()
        if y.upper()=='FIN':
            break
        else:
            while not salir:
                Nombtmp=raw_input('\nNombre a llamada: ')
                if Nombtmp in nom:
                    pos=nom.index(Nombtmp)
                    print '\nLlamando a: ', num[pos]
                else:
                    print '\nError, no tengo el numero'

                e=raw_input('\nPresione la tecla Enter para realizar otra llamada, \nFin para salir\n ')
                if e.upper()=='FIN':
                    salir = True
            break

Add(nom, num)
llamada(nom, num)
