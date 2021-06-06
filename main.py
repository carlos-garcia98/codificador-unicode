#Imports
from os import system

#Declaracion de variables
texto_plano = ""
decision = 0

#Menu
def menu() :
    
    while True :
        
        menu = ''' 
Que desea hacer?:
    1) Codificar.
    2) Descodificar.
    3) Salir.
Utilize el numero correspondiente para seleccionar la accion.
> '''

        decision = int(input(menu))
        
        print("-----------------------------------------------------------------------------------------")
        
        if decision == 1 :
            nota = '''
**Tome en cuenta que el numero 32 es igual a un espacio**
                  '''
            system('cls')
            print(nota)
            ruta(decision)
            break
        
        elif decision == 2 :
            nota = '''
Nota: Si usted tiene una suma de digitos, no se puede descodificar.
                  '''
            system('cls')
            print(nota)
            ruta(decision)
            break
        
        elif decision == 3 :
            system('cls')
            print("Hasta pronto!")
            exit()
            
        else :
            system('cls')
            print("Opcion invalida, intentelo de nuevo.")
            
print("\n")

#Decision
def ruta(decision) :
    
    digito = []
    salida = False
    
    if decision == 1 :
        texto_plano = input("Ingrese el texto a codificar: ")
        codificador(texto_plano)
        
    elif decision == 2 :
        
        instruction = '''
A continuacion, ingresara los digitos uno por uno. Una vez que termine de
ingresar todos los digitos a descodificar por favor, ingrese el numero 0.
          '''
        print(instruction)
        
        while salida == False :
            numeros = int(input("Ingrese el digito Unicode: "))
            digito.append(numeros)
            if numeros == 0 :
                salida = True
                digito.pop()
                
        descodificacion(digito)

#Codificacion
def codificador(texto_plano) :
    
    digito = []
    
    print("\n")
    
    print("El texto codificado es:")
    
    for i in texto_plano :
        caracter = ord(i)
        textoCodifiado = caracter
        print(textoCodifiado, end = " ")
        
    print("\n")
    
    print("La suma de los digitos anteriores es:")
    
    for i in texto_plano :
        caracter = ord(i)
        digito.append(caracter)
    
    print(sum(digito))

#Descodificacion   
def descodificacion(digito) :
            
    print("-----------------------------------------------------------------------------------------")
    
    print("El texto descodificado es:")
    
    for i in digito :
        print(chr(i), end = " ")
        
#Salida a consola

#Bienvenida
print("*************************************************")
print("* Bienvenido al sistema de codificacion Unicode *")
print("*************************************************")

menu()