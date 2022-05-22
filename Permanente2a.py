#importar modulo creado
import moduloperm2a

nombre = input("ingrese nombre del usuario: ").upper()
moduloperm2a.limpCons()
print("Binvenidos al telefono de " + nombre)
moduloperm2a.limpCons(1.5)
i  =True
if moduloperm2a.compClave(nombre) == True:
    while i:
        a = moduloperm2a.menu()
        if a == "1":
            moduloperm2a.calculadora()
        elif a == "2":
            moduloperm2a.contactos()
        elif a == "3":
            moduloperm2a.jugar()
            moduloperm2a.borrar()
        elif a == "4":
            moduloperm2a.feHo()
        elif a =="5":
            moduloperm2a.Apagar()
            break