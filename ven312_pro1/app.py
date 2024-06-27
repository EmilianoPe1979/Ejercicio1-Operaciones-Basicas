#***************************************#
# CENTRO DE BIOTECNOLOGIA AGROPECUARIA  #
# NOMBRE EMILIANO PERILLA AGUILAR       #
# VERSION : 2.0                         #
# Fecha: 25/04/2024                     #
#****************************************


# Este es un programa corto cuya funcion es a traves de dos numeros aleatorios proporcionados
# por la libreria random, generar operaciones como suma, resta, divison, multiplicación y division

# Esta libreria me genera numeros aleatorios

from random import randint
# from colorama import Fore,Back # Importo colorama para color fondo y fuente

a=randint(0,101)
b=randint(0,101)

dato1 = a
dato2 = b 

# print(Fore.BLACK + Back.BLUE)# Defino colores fondo y fuente 

# La funcion saludo ( ) me despliega en pantalla un  mensaje de saludos 
def mensaje_bienvenida():
    print("Binvenidos al Modulo de Operaciones Basicas")


# La funcion suma ( dato1, dato2) suma los numeros almacenados en variables dato1 + dato2
def sumar(dato1, dato2):
    return dato1 + dato2


# La funcion resta ( dato1, dato2) resta los numeros almacenados en variables dato1 - dato2
def restar(dato1, dato2):
    return  dato1 - dato2


# La funcion multiplicación ( dato1, dato2) multiplica los numeros almacenados en variables dato1 * dato2
def multiplicar(dato1, dato2):
    return  dato1 * dato2


# La funcion division ( dato1, dato2) divide los numeros almacenados en variables dato1 / dato2
def dividir( dato1, dato2):
    if dividir != 0:
        return  dato1 / dato2
    else: 
        return "ERROR no se puede dividir por cero"

# El menu de bienvenida donde muestra la operaciones que se realizan, operadando dos numeros aleatorios proporcionados por la libreria Randon  
if __name__ == "__main__":

    print("********INICIO********")
    mensaje_bienvenida()
    print (f"Los numeros aleatorios son : {a,b}")
    print("Operación suma : ",sumar( a,b))
    print("Operación resta: ",restar(a,b))
    print("Operación division: ",dividir(a,b))
    print("Operación multiplicacion: ",multiplicar(a,b))
    print("*********FIN**********")
    print("*****Hasta Pronto**********")