#Tarea 2C: hecha por Luis Guevara Chacón

def divisores (numero): #define los divisores enteros positivos y los retorna en un arreglo

    divisores_enteros = []

    for num in range (1,(numero)):

            if (numero % num) == 0:
                divisores_enteros.append(num)
                #print(sum(divisores_enteros))
                #print(len(divisores_enteros))
    return divisores_enteros


def numero_perfecto (numero): #Recibe un arreglo con los divisores enteros positivos
    if (sum(divisores(numero))==numero):
        print(numero , ": Si es un número Perfecto")

    else:
        print(numero , ": No es un número Perfecto")


numero_perfecto (int(input("Ingrese un número para saber si es perfecto: ")))
