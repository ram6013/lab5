import sys
import os
import matplotlib.pyplot as plt
import random as rd
import numpy as np
from mostrar_laberinto import mostrar_laberinto, guardar_lab, checkear_existencia, recopilar_labs


def definir_size():
    size = (input("Dame un tamaño para el laberinto: "))
    try:
        size = int(size)
    except:
        print("No se aceptan valores distintos de numeros enteros")
        return None
    if (size > 40 or size < 5 ):
        print("No estan permitidos números mayores de 40, menores de 5 o algo distinto de un numero entero.")
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
    final = 0
    while final != 1:
        x = rd.randint(0, size)
        y = rd.randint(0,size)
        if laberinto[x+size,y+size] == 1:
            laberinto[x+size,y+size] = 4
            final = 1

    return laberinto

if __name__=="__main__":
    print("Bienvenido al generador de laberintos!\n")
    size = None
    
    while (size == None):
        size = definir_size()

    #Creamos las carpetas
    carpeta = os.getcwd()
    carpeta = carpeta + "/maze"
    os.makedirs(carpeta, exist_ok=True)
    nombre_base = f"laberinto{size}X{size}"
    carpeta_lab = os.path.join(carpeta, nombre_base)
    os.makedirs(carpeta_lab, exist_ok=True)

    respuesta = checkear_existencia(carpeta_lab, nombre_base)
    if respuesta == 30:
        laberinto = crear_laberintos(size)
        guardar_lab(laberinto, carpeta_lab, nombre_base)
    
    laberintos = recopilar_labs(carpeta_lab)
    mostrar_laberinto(laberintos)
 
    

   
