import matplotlib.pyplot as plt
import numpy as np
import os



def checkear_existencia(carpeta_lab, nombre_base):
    nombre = os.path.join(carpeta_lab, f"{nombre_base}v9.txt")
    conteo_archivos = len([archivo for archivo in os.listdir(carpeta_lab) if os.path.isfile(os.path.join(carpeta_lab, archivo))])
    if not os.path.exists(nombre):
        return 30
    else:
        return conteo_archivos

def guardar_lab(laberinto,carpeta_lab, nombre_base):
    version = 1
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

def recopilar_labs(carpeta):
    laberintos =[]
    archivos = [f for f in os.listdir(carpeta) if f.endswith(".txt") and f.startswith("laberinto")]
    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta, archivo)
        laberinto = np.loadtxt(ruta_archivo, dtype=int)
        laberintos.append(laberinto)
    return laberintos
    


def mostrar_laberinto(laberintos):
    num_laberintos = len(laberintos)
    
    if num_laberintos == 0:
        print("No se encontraron laberintos para mostrar.")
        return

    filas = (num_laberintos + 2) // 3
    columnas = min(3, num_laberintos)
    
    fig, axs = plt.subplots(filas, columnas, figsize=(10, 5))
    
    if filas == 1 and columnas == 1:
        axs = [axs]
    else:
        axs = axs.flatten()  
    
    for i, laberinto in enumerate(laberintos):
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
        
        axs[i].imshow(imagen, cmap='gray', interpolation='none')
        axs[i].set_title(f'Laberinto {i + 1}')
        axs[i].axis('off')  
    
    for j in range(i + 1, len(axs)):
        axs[j].axis('off')
    
    plt.tight_layout()
    plt.show()



