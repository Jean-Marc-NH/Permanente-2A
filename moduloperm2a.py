#importar librerias
from time import sleep
from os import system
import time
import random

#Borrar consola
def borrar(): system("cls")


#Fingir carga
def carga(x = "Cargando"):
    borrar()
    for a in range(3):
        for i in range(3):
            l =[".","..","..."]
            print(x + l[i])
            sleep(.4)
            borrar()
            
#lipiar la consola
def limpCons(x = 1):
    sleep(x)
    system("cls")

#comprobar clave
def compClave(a):
    i = 0
    while i <=5:
        print("Porfavor digite su clave \n")
        x = input(">>>>>>")
        if x == "123456": # verificacion de la clave
            limpCons(.5)
            print("Bienvenido " + a)
            break
        else:
            i += 1
            print("Clave incorrecta")
            limpCons(.5)
    if i == 6:
        print("Muchos intentos Fallidos")
    else:
        return True

#menu de opciones
def menu():
    i = True
    while i:
        print("--Menu--")
        print("(1) Calculadora\n(2) Contactos\n(3) Tres en raya\n(4) Fecha y hora\n(5) Apagar")
        a = input(">>>>>>")
        if a == "1" or a == "2" or a == "3" or a == "4" or a =="5":
            limpCons()
            i = False
            return a
        else:
            print("elige una opccion valida")
            limpCons()

#app de la calculadora
def calculadora():
    carga()
    i  = True
    while i:
        print("--Calculadora--")
        print("(1) Suma\n(2) Resta\n(3) Multiplicacion\n(4) Division")
        a = input(">>>>>>")
        if a == "1":
            limpCons()
            print(sumar())
            limpCons()
            i = False
        elif a == "2":
            limpCons()
            print(resta())
            limpCons()
            i = False
        elif a == "3":
            limpCons()
            print(mult())
            limpCons()
            i = False
        elif a == "4":
            limpCons()
            print(div())
            limpCons()
            i = False
        else:
            print("elige una opccion valida")
            limpCons()

#funciones para la calculadora
#sumar
def sumar():
    i = True
    while i:
        try :
            p = 0
            y = input("Coloque sus numeros ej.(2 4 5): ")
            for a in y.split():
                    p +=  float(a)
            i = False
            return p
        except ValueError:
                print("Coloque solo vaores numericos")
#Multiplicacion
def mult():
    i = True
    while i:
        try :
            p = 1
            y = input("Coloque sus numeros ej.(2 4 5): ")
            for a in y.split():
                    p *=  float(a)
            i = False
            return p
        except ValueError:
                print("Coloque solo vaores numericos")
#division
def div():
    i = True
    while i:
        try:
            a = input("Coloque 2 valores: ")
            b = a.split()
            r = float(b[0])/float(b[1])
            i = False
            return r 
        except ZeroDivisionError :
            print("El segundo valor no puede ser 0")
        except ValueError:
            print("sus valores no son numericos")
#resta
def resta():
    i = True
    while i:
        try : 
            a = input("Coloque sus numeros ej.(2 4 5): ")
            b = a.split()
            p = 0
            c = b.pop(0)
            for i in b:
                p += int(i)
            p = int(c) - p
            i = False
            return p 
        except ValueError:
            print("sus valores no son numericos")

#app de contactos
def contactos():
    carga()
    dic = {}
    i = True
    while i:
        print("--Contactos--")
        print("(1) Añadir\n(2) Ver\n(3) Salir")
        a = input(">>>>>>")
        if a == "1" :
            limpCons(.5)
            añadir(dic)
            limpCons(.5)
        elif a == "2":
            limpCons(.5)
            ver(dic)
            print("\n\n\n")
        elif a == "3":
            limpCons()
            menu()
            i = False
        else:
            print("elige una opccion valida")
            limpCons()
#Añadir contactos
def añadir(x):
    a = input("Nombre: ")
    x[a] = input("Numero: ")
    return x
#Mostrar contactos
def ver(a):
    for i,x in a.items():
        print(f"{i}:{x}")
#ver la fecha y hora
def feHo():
    carga()
    print("--Fecha y Hora--")
    a = time.strftime("%H:%M:%S")
    b = time.strftime("%d/%m/%y")
    print(f"La hora es: {a}\nLa fecha es: {b}")
    sleep(2)
    limpCons()
    menu()

import random

#posiciones del tablero
tab = ["0","1","2","3","4","5","6","7","8"]
#imprimir tablero
def print_tablero(tablero):
    assert len(tablero) == 9
    print("|{}|{}|{}|".format(*tablero[:3]))
    print("|{}|{}|{}|".format(*tablero[3:6]))
    print("|{}|{}|{}|".format(*tablero[6:]))
    print("------------")

def existe_ganador(tab):
    # Buscando un ganador en lineas verticales 
    for col in range(3): # col = {0,1,2}
        if tab[col] == tab[col+3] and tab[col] == tab[col+6]:
            return True
    # Buscando un ganador en lineas horizontales
    for fila in range(0,9,3): # file = {0,3,6}
        if tab[fila] == tab[fila+1] and tab[fila] == tab[fila+2]:
            return True
    # Buscando un ganador en las diagonales
        if (tab[0] == tab[4] and tab[0] == tab[8]) or (tab[2]==tab[4] and tab[2]==tab[6]):
            return True
    return False
#Buscar si las casillas estan ocupadas
def casillas_disponibles(tablero):
    disponibles = []
    for casilla in tablero:
        if casilla not in ["X","O"]:
            disponibles.append(int(casilla))
    return disponibles


def comp_mov(tablero):
    movimientos_disponibles = casillas_disponibles(tablero) # detectar las casillas disponibles
    casilla = escoger_casilla(movimientos_disponibles, tablero) # escoger una de esas casillas (aleatoria)
    return casilla

def escoger_casilla(casillas_disponibles, tablero):
    gana_usuario = False
    gana_comput = False
    
    pos1 = -1
    pos2 = -1 
    
    for casilla in casillas_disponibles:
        tablero1 = tablero.copy()
        tablero2 = tablero.copy()

        tablero1 = marcar_casilla(tablero1, casilla, "X") # USUARIO
        tablero2 = marcar_casilla(tablero2, casilla, "O") # MÁQUINA

        #print(tablero1, tablero2)
        # Tablero para el usuario
        if existe_ganador(tablero1) == True:
            pos1 = casilla
            gana_usuario = True
            print("Gana el usuario!")
            break

        # Tablero para el computador
        if existe_ganador(tablero2) == True:
            pos2 = casilla
            gana_comput = True
            break
      
    # print(gana_comput, gana_usuario, pos1, pos2)
    if gana_comput == True:
        return pos2
    elif gana_usuario == True:
        return pos1
    else:
        return random.choice(casillas_disponibles)

def marcar_casilla(tablero, casilla, simbolo):
    tablero[casilla] = simbolo
    return tablero

def jugar():
    tablero = ["0","1","2","3","4","5","6","7","8"]
    i = 0

    # i = {0,1,2,3,4,5,6,7,8}
    while i < 9:
        borrar()
        print_tablero(tablero)

        if i % 2 == 0: # par
            try:
                casilla = int(input("Jugador X (0-8): "))
            except:
                print("Ingrese un entero!")
                continue
            
            if casilla in casillas_disponibles(tablero):
                tablero = marcar_casilla(tablero, casilla, "X")
            else:
                print("Elige otra casilla!")
                continue

            if existe_ganador(tablero):
                print("Gana el jugador X!")
                break
        else: # impar
            casilla = comp_mov(tablero)
            print("Jugador O: ")
            #if casilla in casillas_disponibles(tablero):
            tablero = marcar_casilla(tablero, casilla, "O")

            if existe_ganador(tablero):
                print("Gana el jugador O!")
                break
          
        i+=1
#Apagar telefono
def Apagar():
    carga("Apagando")

    