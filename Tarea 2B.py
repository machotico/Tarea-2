#Tarea 2B: hecha por Luis Guevara Chacón

def is_in_range(num, min, max): #establece si un número está en rango y devuelve un 'si' o un 'no'

    for y in range (min,max+1):
        #print(y)
        if y == num:
            respuesta = ": Si"
            #break
            return respuesta

        else:
            respuesta = ": No"

    return respuesta

def imprime_num_rango (): # Establece la interaccion con el usuario y ejecuta la funcion de 'rango'
    numero = int(input("Ingrese el número incógnita: "))
    mínimo = int(input("Ingrese el límite inferior: "))
    máximo = int(input("Ingrese el límite superior: "))

    print("Esta el número en rango entre",mínimo,"y",máximo, is_in_range(numero,mínimo,máximo))


imprime_num_rango()
