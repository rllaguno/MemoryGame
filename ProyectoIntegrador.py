#Proyecto Integrador, Pensamiento Computacional para la Ingeniería
#Rodrigo Llaguno A01198067
#Jorge Alejandro Nuñez A00833455

import time
import random

def main():
    startup()
    nivel = get_nivel()
    tipo = get_tipo()
    if nivel == 1:
        facil(tipo, nivel)
    elif nivel == 2:
        normal(tipo, nivel)
    elif nivel == 3:
        dificil(tipo, nivel)
    elif nivel == 4:
        experto(tipo, nivel)
    
def startup():
    print('\n')
    print("Proyecto Integrador: Juego de Repetición")
    print("Creado por Jorge Nuñez y Rodrigo Llaguno")
    print('\n')
    print("¿Deseas leer las instrucciones?")
    instrucciones = input("Si o No: ")
    instrucciones = instrucciones.lower()
    instrucciones = instrucciones.strip()
    print('\n')

    if instrucciones == "si" or instrucciones == "s":
        print("El objetivo del juego es memorizar los números o letras aleatorias que se mostrarán en la pantalla.")
        time.sleep(3)
        print("Después de que se hayan mostrado todos los valores, tendrás que escribir dichas letras o números en el mismo orden, uno por uno.")
        time.sleep(4.5)
        print("Una vez que hayas ingresado tu respuesta, el juego te dirá si lo repetiste de manera correcta o no.")
        time.sleep(3)
        print("Si lo ingresaste correctamente, pasarás al siguiente nivel hasta completar el juego.")
        time.sleep(3)
        print("¡Buena Suerte!")
        print('\n')
        time.sleep(2)
        return
    else:
        return

def facil(tipo, nivel): #8 niveles, 3 flechas, 18 segundos
    if tipo == 1:
        print('¡El juego esta por comenzar, pon atención a los números!')
        print('\n'*10)
    elif tipo == 2:
        print('¡El juego esta por comenzar, pon atención a las letras!')
        print('\n'*10)
    time.sleep(5)
    matriz = get_inputs(tipo, nivel)
    cantidad = 3
    num_level = 8
    game = juego(matriz, nivel, tipo, cantidad, num_level)

def normal(tipo, nivel): #7 niveles, 4 flechas, 12 segundos
    if tipo == 1:
        print('¡El juego esta por comenzar, pon atención a los números!')
        print('\n'*10)
    elif tipo == 2:
        print('¡El juego esta por comenzar, pon atención a las letras!')
        print('\n'*10)
    time.sleep(5)
    matriz = get_inputs(tipo, nivel)
    cantidad = 4
    num_level = 7
    game = juego(matriz, nivel, tipo, cantidad, num_level)    

def dificil(tipo, nivel): #6 niveles, 5 flechas, 7 segundos
    if tipo == 1:
        print('¡El juego esta por comenzar, pon atención a los números!')
        print('\n'*10)
    elif tipo == 2:
        print('¡El juego esta por comenzar, pon atención a las letras!')
        print('\n'*10)
    time.sleep(5)
    matriz = get_inputs(tipo, nivel)
    cantidad = 5
    num_level = 6
    game = juego(matriz, nivel, tipo, cantidad, num_level)

def experto(tipo, nivel): #5 niveles, 6 flechas, 7 segundos
    if tipo == 1:
        print('¡El juego esta por comenzar, pon atención a los números!')
        print('\n'*10)
    elif tipo == 2:
        print('¡El juego esta por comenzar, pon atención a las letras!')
        print('\n'*10)
    time.sleep(5)
    matriz = get_inputs(tipo, nivel)
    cantidad = 6
    num_level = 5
    game = juego(matriz, nivel, tipo, cantidad, num_level)

def get_inputs(tipo, nivel):

    if nivel == 1:
        matriz = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
        ]
        cantidad = 3
        num_level = 8

    elif nivel == 2:
        matriz = [
        [],
        [],
        [],
        [],
        [],
        [],
        []
        ]
        cantidad = 4
        num_level = 7

    elif nivel == 3:
        matriz = [
        [],
        [],
        [],
        [],
        [],
        [],
        ]
        cantidad = 5
        num_level = 6

    elif nivel == 4:
        matriz = [
        [],
        [],
        [],
        [],
        []
        ]
        cantidad = 6
        num_level = 5

    if tipo == 1: #Conseguir flechas de un nivel
        for i in range(num_level): 
            for j in range(cantidad):
                matriz[i].append(random.randint(1,4))

    elif tipo == 2: #Conseguir letras de un nivel
        for i in range(num_level): 
            for j in range(cantidad):
                letters = 'abcdefghijklmnopqrstuvwxyz'
                matriz[i].append(random.choice(letters))
    
    return matriz

def juego(matriz, nivel, tipo, cantidad, num_level):
    m_respuesta = []
    
    puntos = 0
    diff_time = 0
    initial_time = time.time
    while puntos >= 0 and puntos < num_level:
        for i in range(num_level):
            for j in range(cantidad):
                if tipo == 1:
                    print('\n')
                    print(matriz[i][j])
                    time.sleep(2)
                    print('\n'*100)
                elif tipo == 2:
                    print('\n')
                    print(matriz[i][j])
                    time.sleep(2)
                    print('\n'*100)
            for _ in range(cantidad):
                if tipo == 1:
                    # medir tiempo por input, si se pasa salir y mostrar mensaje
                    respuesta = input("Valor " + str(_+1) + ": ")
                    if respuesta == "":
                        print("Numero Inválido")
                        exit()
                    respuesta = int(respuesta)
                    m_respuesta.append(respuesta)
                elif tipo == 2:
                    respuesta = str(input("Valor " + str(_+1) + ": "))
                    if respuesta == "":
                        print("Letra Inválida")
                        exit()  
                    m_respuesta.append(respuesta)
                
            if m_respuesta == matriz[i]: 
                print('\n')
                print("Nivel Completado")
                puntos += 1
                m_respuesta = [] 
            else:
                print('\n')
                print("Nivel Fallido, la respuesta era: " + str(matriz[i]))
                puntos = -1
                break
            
        if puntos == -1: 
            break
        elif puntos == num_level-1 or num_level:
            print("Completaste el Juego!")
            break
    print("Fin del Juego!") 
        
def get_nivel():
    nivel = 0
    
    while nivel <= 0 or nivel > 4:
        print("Nivel 1: Facil")
        print("Nivel 2: Normal")
        print("Nivel 3: Dificil")
        print("Nivel 4: Experto")
        nivel = int(input("Selecciona la dificultad: " ))
        print('\n')
        
    return nivel
    
def get_tipo():
    tipo = 0

    while tipo <= 0 or tipo > 2:
            print("Tipo de Juego 1: Numeros")
            print("Tipo de Juego 2: Letras")
            tipo = int(input("Selecciona el tipo de juego: "))
            print('\n')
    return tipo

main()