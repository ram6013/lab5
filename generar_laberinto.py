import sys
import matplotlib.pyplot as plt
import random as rd
import numpy as np
from mostrar_laberinto import mostrar_laberinto, guardar_lab, checkear_existencia, leer_lab


def definir_size():
    size = (input("Dame un tamaño para el laberinto: "))
    try:
        size = int(size)
    except:
        print("No se aceptan valores distintos de numeros enteros")
        return None
    if (size > 40 or size <= 0 ):
        print("No estan permitidos números mayores de 40, menores e iguales 0 o distintos de un numero.")
        return None
    else:
        return size
        


def generar_caminos(laberinto, x, y):
    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Arriba, derecha, abajo, izquierda
    rd.shuffle(direcciones)

    for dx, dy in direcciones:
        nx, ny = x + dx * 2, y + dy * 2  

        if 0 <= nx < laberinto.shape[0]-1 and 0 <= ny < laberinto.shape[1]-1:
            if laberinto[nx][ny] == 0:  
                laberinto[x + dx][y + dy] = 1  # Abre el camino intermedio
                laberinto[nx][ny] = 1  # Marca la nueva celda con camino
                generar_caminos(laberinto, nx, ny)

            


def crear_laberintos(size: int):    
    laberinto = np.zeros((size * 2 + 1, size * 2 + 1)) 
    laberinto[0, 1] = 1  #1 significa camino
    generar_caminos(laberinto, 1, 1) 
    
    if  laberinto[size,size*2-1] != 0:
        laberinto[size,size*2-1] = 4 #significa final
    else:
        laberinto[size -1, size*2-1]=4
    return laberinto

if __name__=="__main__":
    print("Bienvenido al generador de laberintos!\n")
    size = None
    while (size == None):
        size = definir_size()
    respuesta = checkear_existencia(size)
    if respuesta == 30:
        laberinto = crear_laberintos(size)
        guardar_lab(size, laberinto)
    else:
        pass
    mostrar_laberinto(laberinto)
 
    

   
