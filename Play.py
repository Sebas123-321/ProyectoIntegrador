import os
import sys
import msvcrt

class Juego:
    def __init__(self, nombre_jugador):
        self.nombre_jugador = nombre_jugador
        self.mapa = self.cargar_mapa("C:/Users/Juanse/Documents/AdaSchool/Proyecto_Integrador/Laberinto/mapa.txt")
        self.filas = len(self.mapa)
        self.columnas = len(self.mapa[0])
        self.jugador_posicion = None

    def cargar_mapa(self, archivo):
        with open(archivo, "r") as f:
            return [list(line.strip()) for line in f.readlines()]

    def mostrar_mapa(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Jugador:", self.nombre_jugador)
        for fila in self.mapa:
            print("".join(fila))

    def encontrar_jugador(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.mapa[i][j] == ".":
                    self.jugador_posicion = (i, j)
                    return

    def mover_jugador(self, direccion):
        movimientos = {
            "w": (-1, 0),  # Arriba
            "s": (1, 0),   # Abajo
            "a": (0, -1),  # Izquierda
            "d": (0, 1)    # Derecha
        }

        nueva_fila, nueva_columna = tuple(
            sum(x) for x in zip(self.jugador_posicion, movimientos[direccion])
        )

        if (
            0 <= nueva_fila < self.filas
            and 0 <= nueva_columna < self.columnas
            and self.mapa[nueva_fila][nueva_columna] == "."
        ):
            self.mapa[self.jugador_posicion[0]][self.jugador_posicion[1]] = " "
            self.mapa[nueva_fila][nueva_columna] = "@"
            self.jugador_posicion = (nueva_fila, nueva_columna)

    def jugar(self):
        self.mostrar_mapa()
        self.encontrar_jugador()
        while True:
            if msvcrt.kbhit():
                tecla = msvcrt.getch().decode().lower()
                if tecla in ("w", "s", "a", "d"):
                    self.mover_jugador(tecla)
                    self.mostrar_mapa()
                elif tecla == "q":
                    print("¡Juego terminado!")
                    break

def obtener_nombre_jugador():
    nombre = input("Ingrese su nombre: ")
    return nombre

if __name__ == "__main__":
    nombre_jugador = obtener_nombre_jugador()
    juego = Juego(nombre_jugador)
    juego.jugar()
