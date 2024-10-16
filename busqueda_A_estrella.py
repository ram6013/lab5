from funciones_auxiliares import *
import os
import heapq
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def distancia_manhattan(nodo1, nodo2):
    return abs(nodo1[0] - nodo2[0]) + abs(nodo1[1] - nodo2[1])

def astar_visual(grafo, laberinto, inicio, fin, img):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio))
    padres = {inicio: None}
    costes = {inicio: 0}
    explorados = set()

    while cola_prioridad:
        _, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == fin:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual)
                nodo_actual = padres[nodo_actual]
            return camino[::-1]  
        
        explorados.add(nodo_actual)
        for vecino in grafo[nodo_actual]:
            nuevo_coste = costes[nodo_actual] + 1
            if vecino not in costes or nuevo_coste < costes[vecino]:
                costes[vecino] = nuevo_coste
                prioridad = nuevo_coste + distancia_manhattan(vecino, fin)
                heapq.heappush(cola_prioridad, (prioridad, vecino))
                padres[vecino] = nodo_actual

        laberinto[nodo_actual[0]][nodo_actual[1]] = 2  
        img.set_data(laberinto)
        plt.draw()
        plt.pause(0.1)  

    return None  

def encontrar_camino():
    ruta = os.getcwd()
    size = input("¿Qué tamaño quieres el laberinto? ")
    version = input("¿Qué versión quieres? ")
    ruta = ruta + f"/maze/laberinto{size}X{size}/laberinto{size}X{size}v{version}.txt"
    
    try:
        laberinto = leer_laberinto(ruta)
        laberinto = [[int(c) for c in fila if c.isdigit()] for fila in laberinto]
    except FileNotFoundError:
        print(f"El fichero {ruta} no se encontró.")
        return
    
    grafo = convertir_cuadricula_a_grafo(laberinto)

    inicio = None
    fin = None
    
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == 1 and inicio is None:  
                inicio = (i, j)
            if laberinto[i][j] == 4:  
                fin = (i, j)
    
    
    fig, ax = plt.subplots()
    cmap = mcolors.ListedColormap(['white', 'black', 'white', 'green', 'blue'])
    bounds = [-1, 0, 1, 2, 3, 4]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    img = ax.imshow(laberinto, cmap=cmap, norm=norm)
    plt.ion()
    plt.show()

    camino = astar_visual(grafo, laberinto, inicio, fin, img)
    
    if camino:
        for nodo in camino:
            laberinto[nodo[0]][nodo[1]] = 5  
            img.set_data(laberinto)
            plt.draw()
            plt.pause(0.1)
    else:
        print("No se encontró un camino.")

    plt.ioff()
    plt.show()

encontrar_camino()
