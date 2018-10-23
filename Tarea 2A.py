#Tarea 2A: hecha por Luis Guevara Chacón

def recibe_numero (): #recibe un entero del teclado y lo regresa

    return (int(input("Ingrese un número: ")))

def recibe_multiples_numeros(cantidad_numeros): #recibe la cantidad de números que se van a ingresar y usando la función anterior los regresa en un arreglo

    arreglo = [None]*cantidad_numeros

    for y in range (0,cantidad_numeros):

        arreglo [y] = recibe_numero() #test

    return arreglo

def retorna_mayor(): # Funcion organizadora y de interacción con el usuario

    cuantos_numeros = (int(input("Ingrese la cantidad de números que usará para calcular el mayor: ")))

    print ("El mayor número es:", max (recibe_multiples_numeros(cuantos_numeros)))

retorna_mayor()
