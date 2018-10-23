#Tarea 2D: hecha por Luis Guevara Chacón

def recibe_numero (): #recibe un entero del teclado y lo regresa
    return (int(input("Ingrese un número: ")))

def retorna_redondeados(número): #redondea a unidades
    temp = número % 10
    if (temp >= 5):
        número = número + (10-temp)
    else:
        número = número - temp

    #print(número)
    return número

def suma (num1,num2,num3): # Suma 3 números
    return num1 + num2 + num3;


def round_sum(num_a, num_b, num_c):

    suma_redondeada = suma(retorna_redondeados(num_a),retorna_redondeados(num_b),retorna_redondeados(num_c))
    #return print("El Resultado de la suma redondeada es: ", suma_redondeada)
    return suma_redondeada

print ("El Resultado de la suma redondeada a nivel de unidades es: ",round_sum(recibe_numero(),recibe_numero(),recibe_numero()))
