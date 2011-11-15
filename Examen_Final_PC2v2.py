
#EXAMEN FINAL PRACTICO
#PROGRAMACION CIENTIFICA 2

#INTEGRANTES DE GRUPO:
#JORGE LUIS PEREZ CANTO  201024865
#CARLOS GEOVANI MEJIA PINEDA  201016020
#ERICK DANIEL ZAMORA LOPEZ 201016261


print "Cargando..."

import MySQLdb
from pylab import *


#Conectando al servidor

try:
    #Intentamos conectarnos con el servidor
    db = MySQLdb.connect("localhost","root","")
    # Preparamos un objeto con el metodo cursor.
    cursor = db.cursor() 
except:
    #De producirse un error en la coneccion, mostramos el siguiente mensaje.
    print "\nNo se ha podido establecer coneccion con el servidor.\n"
    raw_input()
    #Luego terminamos el programa.
    exit


#Creacion de base de datos
    
try:
    #Preparamos una consulta sql para crear una base de datos llamada: efpem
    dbEfpem="CREATE DATABASE efpem"
    
    #Preparamos una consulta para usar dicha base de datos.
    dbUSE="USE efpem"

    #Preparamos una consulta para Crear la Tabla Alumnos y sus repectivos campos
    crearTabla="Create Table Alumnos (Carnet INT(8), Nombre VARCHAR(15), Apellido VARCHAR(15), \
                        Fisica INT, Quimica INT, Lenguaje INT, Matematica INT, Computacion INT,ProgramacionCientifica2 INT);"
    try:
       #Ejecutamos las consultas utilizando el metodo Excecute()
        cursor.execute(dbEfpem)
        cursor.execute(dbUSE)
        cursor.execute(crearTabla)
        #Confirmamos los cambios.
        db.commit()
        print "\nLa base de datos ha sido creada con exito.\n"
        raw_input()
        #Desconectamos la base de datos.
        db.close()
    except:
        #En caso de error:
        db.rollback()
    
except:
    print


#Coneccion a la base de datos "efpem"
        
try:
    db = MySQLdb.connect("localhost","root","","efpem" )
    cursor = db.cursor()
except:
    print "\nNo se ha podido establecer conección con la base de datos.\n"
    raw_input()
    exit


#Funcion para ingresar datos en la tabla Alumnos
def ingresar():
    #Solicitamos el ingresos de los datos y las almacenamos en sus repectivas variables
    print "\nIngrese los datos que se le solicitan a continuacion: \n"
    Carnet = raw_input("Carnet: ")
    Nombre = raw_input("Nombre: ")
    Apellido = raw_input("Apellido: ")
    
    try:
        print "\nIngrese las calificaciones de los siguientes cursos: \n"
        Fisica = int(raw_input("Fisica: "))
        Quimica = int(raw_input("Quimica: "))
        Lenguaje = int(raw_input("Lenguaje: "))
        Matematica = int(raw_input("Matematica: "))
        Computacion= int(raw_input("Computacion: "))
        Programacion = int(raw_input ("ProgramacionCientifica2: "))
    except:
        #En caso de error, mostramos un mensaje y regresamos al menu principal.
        print "\nError. Por favor ingrese numeros enteros."
        RegresarMenu()

    #Preparamos la consulta para ingresar los valores en la tabla Alumnos
    sql ="INSERT INTO Alumnos (Carnet, Nombre, Apellido, Fisica, Quimica, Lenguaje, Matematica, Computacion,ProgramacionCientifica2) \
            VALUES ('%s', '%s', '%s', '%s','%s','%s','%s','%s','%s')" % \
           (Carnet, Nombre, Apellido, Fisica, Quimica, Lenguaje, Matematica, Computacion,Programacion)

    try:
       cursor.execute(sql) #Ejecutamos la consulta
       db.commit() #Guardamos los cambios
    except:
       print "\nSe ha producido un error durante la ejecucion."
       db.rollback()
    RegresarMenu()

#Funcion para mostrar todos los datos de la tabla Alumnos.
    
def mostrar():
    #Preparamos la consulta, para seleccionar todos los registros de la tabla Alumnos
    sql ="SELECT * FROM alumnos order by Apellido"
    try:
        #Ejecutamos la consulta
        cursor.execute(sql)
    except:
        print "\nSe ha producido un error durante la ejecucion."
        RegresarMenu()    
    try:
        #Obtenemos el resultado de las consultas:
        results = cursor.fetchall()
        for row in results:
            #Obtenemos el valor de cada campo.
            Carnet = row[0]
            Nombre = row[1]
            Apellido = row[2]
            Fisica = row[3]
            Quimica = row[4]
            Lenguaje = row[5]
            Matematica = row[6]
            Computacion = row[7]
            Programacion = row [8]           
            #Mostramos el resultado obtenido.
            print " "
            print "\nDatos Personales: \n", "\nCarnet =", row[0],"\nNombre =",row[1],"\nApellido =",row[2], "\n\nNotas de Cursos: "
            print "\nFisica =",row[3],"\nQuimica =",row[4],"\nLenguaje =",row[5],"\nMatematica =",row[6],"\nComputacion =",row[7],"\nProgramacionCientifica2 =" ,row[8]
    except:
        print "\nError: unable to fecth data"
    RegresarMenu()



#Funcion para buscar datos por numero de carnet
    
def consultaCarne():
    carnetB = raw_input("\nNumero de carne del alumno a buscar: ")
    #Preparamos la consulta, donde mostranos todos los registros de la tabla alumnos donde el carnet sea igual al valor ingresado por el usuario.
    sql ="SELECT * FROM Alumnos WHERE Carnet = '%s'" % (carnetB)
    try:
        cursor.execute(sql)
    except:
        print "\nSe ha producido un error durante la ejecucion."
        RegresarMenu()
    try:
        results = cursor.fetchall()
        for row in results:
            Carnet = row[0]
            Nombre = row[1]
            Apellido = row[2]
            Fisica = row[3]
            Quimica = row[4]
            Lenguaje = row[5]
            Matematica = row[6]
            Computacion = row[7]
            Programacion = row[8]              
            print " "
            print "\nDatos Personales: \n", "\nCarnet =", row[0],"\nNombre =",row[1],"\nApellido =",row[2], "\n\nNotas de Cursos: "
            print "\nFisica =",row[3],"\nQuimica =",row[4],"\nLenguaje =",row[5],"\nMatematica =",row[6],"\nComputacion =",row[7],"\nProgramacionCientifica2 =",row[8]
    except:
        print "\nError: unable to fecth data"
    RegresarMenu()    
    

#Funcion para buscar datos por Nombre.
    
def consultaNombre():
    nombreB = raw_input("\nNombre del alumno a buscar: ")
    #Preprarmos la consulta para mostrar todos los registros de la tabla Alumnos donde el nombre sea igual al ingresado por el usuario.
    sql ="SELECT * FROM Alumnos WHERE Nombre = '%s'" % (nombreB)
    try:
        cursor.execute(sql)
    except:
        print "\nSe ha producido un error durante la ejecucion."
        RegresarMenu()
    try:
        results = cursor.fetchall()
        for row in results:
            Carnet = row[0]
            Nombre = row[1]
            Apellido = row[2]
            Fisica = row[3]
            Quimica = row[4]
            Lenguaje = row[5]
            Matematica = row[6]
            Computacion = row[7]
            Programacion = row[8]               
            print " "
            print "\nDatos Personales: \n", "\nCarnet =", row[0],"\nNombre =",row[1],"\nApellido =",row[2], "\n\nNotas de Cursos: "
            print "\nFisica =",row[3],"\nQuimica =",row[4],"\nLenguaje =",row[5],"\nMatematica =",row[6],"\nComputacion =",row[7],"\nProgramacionCientifica2 =",row[8]
    except:
        print "Error: unable to fecth data"
    RegresarMenu()


#Funcion para graficar calificaciones.
    
def graficas ():
    carnetA = raw_input("\nIngrese el numero de carnet del alumno: ")
    #Preparamos la consulta para selecionar el registro del alumno a graficar
    sql ="SELECT * FROM Alumnos WHERE Carnet = '%s'" % (carnetA)
    
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        nombrealumno = []
        #Obtenemos los datos.
        for row in results:
            Carnet = row[0]
            Nombre = row[1]
            Apellido = row[2]
            Fisica = row[3]
            Quimica = row[4]
            Lenguaje = row[5]
            Matematica = row[6]
            Computacion = row[7]
            Programacion = row[8]               
    except:
        print "\nError: unable to fecth data"

    try:
        nombrealumno.append("Notas del alumno(a) : " + Nombre + " " + Apellido)
        #Datos del alumno a graficar:
        data = [Fisica, Quimica, Lenguaje, Matematica, Computacion,Programacion]
        #Arreglo para el eje X
        xlocations = array(range(len(data)))+0.5
        #Ancho
        width = 0.5
        #Tipo de grafica y sus valores
        bar(xlocations, data,  width=width)
        #Rango en el eje X
        xlim(0, xlocations[-1]+width*2)
        #Rango en el eje Y
        ylim(0,100)
        #Titulo de la Grafica
        title(nombrealumno)
        grid (True)
        #Etiquetas
        label=["Fisica","Quimica","Lenguaje","Matematica","Compu","PrograCien2"]
        xticks(xlocations + width / 2, label)
        print " "
        print "A continuacion se mostraran las notas del alumno(a) en una grafica..."
        print " "
        #Mostramos la grafica:
        show()
    except:
        print "\nRegistro no encontrado.\n"
    RegresarMenu()



#Funcion para modificar algun dato.
    
def actualizar():
    carnetA = raw_input("\nIngrese el numero de carnet del alumno: ")
    sql ="SELECT * FROM alumnos WHERE Carnet = '%s'" % (carnetA)
    
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            Carnet = row[0]
            Nombre = row[1]
            Apellido = row[2]
            Fisica = row[3]
            Quimica = row[4]
            Lenguaje = row[5]
            Matematica = row[6]
            Computacion = row[7]
            Programacion = row[8]               
            print " "
            print "\nDatos Personales: \n", "\nCarnet =", row[0],"\nNombre =",row[1],"\nApellido =",row[2], "\n\nNotas de Cursos: "
            print "\nFisica =",row[3],"\nQuimica =",row[4],"\nLenguaje =",row[5],"\nMatematica =",row[6],"\nComputacion =",row[7],"\nProgramacionCientifica2 =",row[8]
    except:
        print "Error: unable to fecth data"
            
    print " "
    #Solicitamos el ingreso de los nuevos valores.
    print "\nIngrese las nuevas notas de los cursos: \n"
    FisicaA = int(raw_input("Fisica: "))
    QuimicaA = int(raw_input("Quimica: "))
    LenguajeA = int(raw_input("Lenguaje: "))
    MatematicaA = int(raw_input("Matematica: "))
    ComputacionA = int(raw_input("Computacion: "))
    ProgramacionA = int(raw_input("ProgramacionCientifica2: "))                       

    #Preparamos la consulta sql para modificar los datos de la tabla alumnos,
    #donde el numero de carnet sea igual al ingresado por el usuario anteriormente.
    sql ="UPDATE alumnos SET Fisica = '%s',Quimica='%s',Lenguaje='%s',Matematica='%s',Computacion='%s',ProgramacionCientifica2='%s' \
            WHERE Carnet = '%s'" % (FisicaA, QuimicaA, LenguajeA, MatematicaA, ComputacionA,ProgramacionA,carnetA)
    try:
        #Ejecutamos
        cursor.execute(sql)
        #Guardamos
        db.commit()
    except:
        db.rollback()
    RegresarMenu()
    


def RegresarMenu():
    print " "
    raw_input ("\nPresione cualquier tecla para regresar al menu anterior...")
    
    Menu()

#Menu Principal de Programa
    
def Menu():
    
    print """
    ________________________________________________________________________
                                                                                                                                                           
                    Opciones disponibles :                                                             
    ________________________________________________________________________
                                                                                                                                                            
            1.  -  Ingresar un alumno con todas las calificaciones.
            2.  -  Consultar todos los alumnos en la base de datos.
            3.  -  Consultar un alumno por su numero de carnet.      
            4.  -  Consultar un alumno por su nombre registrado.
            5.  -  Elaborar grafica de las calificaciones de un alumno.
            6.  -  Modificar las calificaciones de un alumno.
            7.  -  Finalizar el programa.
    ________________________________________________________________________
"""

    try:
        opcion = int(raw_input("Ingrese el numeral correspondiente a su eleccion: "))
    except:
        
        print "\nError: El valor ingresado no es de tipo numerico, por favor vuelva a intentarlo."
        RegresarMenu()

    try:
        
        if opcion == 1:
            ingresar()
        elif opcion == 2:
            mostrar()
        elif opcion == 3:
            consultaCarne()
        elif opcion == 4:
            consultaNombre()
        elif opcion == 5:
            graficas()
        elif opcion == 6:
            actualizar()
        elif opcion == 7:
            print "El programa se esta cerrando..."
            try:
                db.close()
                exit()
            except:
                exit
        else:
            print "Error: El valor ingresado esta fuera de rango."
            RegresarMenu()
                
    except:
        print "\nError."
        RegresarMenu()

Menu()
