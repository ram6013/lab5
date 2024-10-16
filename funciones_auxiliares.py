import os

def leer_laberinto(fichero):
    if os.path.isfile(fichero):
        with open(fichero, 'r') as file:
            laberinto = [list(line.strip()) for line in file.readlines()]
        return laberinto
    else:
        raise FileNotFoundError(f"El archivo {fichero} no existe.")

def convertir_cuadricula_a_grafo(laberinto):
    """Convierte la cuadrícula del laberinto a un grafo donde las celdas transitables están conectadas."""
    filas = len(laberinto)
    columnas = len(laberinto[0])
    grafo = {}

    for i in range(filas):
        for j in range(columnas):
            if laberinto[i][j] == 1 or laberinto[i][j] == 4:  # Solo transitables (1 o el 4 que es el final)
                grafo[(i, j)] = []
                # Verificar vecinos arriba, abajo, izquierda y derecha
                if i > 0 and (laberinto[i-1][j] == 1 or laberinto[i-1][j] == 4):  # Arriba
                    grafo[(i, j)].append((i-1, j))
                if i < filas - 1 and (laberinto[i+1][j] == 1 or laberinto[i+1][j] == 4):  # Abajo
                    grafo[(i, j)].append((i+1, j))
                if j > 0 and (laberinto[i][j-1] == 1 or laberinto[i][j-1] == 4):  # Izquierda
                    grafo[(i, j)].append((i, j-1))
                if j < columnas - 1 and (laberinto[i][j+1] == 1 or laberinto[i][j+1] == 4):  # Derecha
                    grafo[(i, j)].append((i, j+1))
    
    return grafo


