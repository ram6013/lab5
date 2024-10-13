import matplotlib.pyplot as plt
import numpy as np
import os

def leer_lab(nombre):
    matriz_leida = np.loadtxt(nombre, dtype=int)
    mostrar_laberinto(matriz_leida)

def checkear_existencia(size):
    carpeta = "/home/ramon/Documentos/Unie/IA/lab5/maze"
    nombre_base = f"laberinto{size}X{size}"
    carpeta_lab = os.path.join(carpeta, nombre_base)
    os.makedirs(carpeta_lab, exist_ok=True)
    nombre = os.path.join(carpeta_lab, f"{nombre_base}v9.txt")
    conteo_archivos = len([archivo for archivo in os.listdir(carpeta_lab) if os.path.isfile(os.path.join(carpeta_lab, archivo))])
    if not os.path.exists(nombre):
        return 30
    else:
        return conteo_archivos

def guardar_lab(size, laberinto):
    version = 1
    carpeta = os.getcwd()
    carpeta = carpeta + "/maze"
    print(carpeta)
    nombre_base = f"laberinto{size}X{size}"
    
    os.makedirs(carpeta, exist_ok=True)
    carpeta_lab = os.path.join(carpeta, nombre_base)
    os.makedirs(carpeta_lab, exist_ok=True)
    
    while True:
        nombre = os.path.join(carpeta_lab, f"{nombre_base}v{version}.txt")
        if not os.path.exists(nombre):
            break
        version += 1
    if (version > 9):
        print("Se ha generado el máximo número de laberintos.")
            
    else:
        np.savetxt(nombre, laberinto, fmt='%d')
        print(f"Archivo guardado como: {nombre}")


def mostrar_laberinto(laberinto):
    imagen = []
    for fila in laberinto:
        fila_visual = []
        for celda in fila:
            if celda == 0:
                fila_visual.append(0)
            elif celda == 4:
                fila_visual.append(4)
            else:
                fila_visual.append(1)
        imagen.append(fila_visual)

    plt.imshow(imagen, cmap='gray', interpolation='none')
    plt.title('Visualización del laberinto generado')
    plt.axis('off')
    plt.show()



