import os
from pathlib import Path
from os import system

def ejecutar_programa():
    mi_ruta = Path(Path.home(), 'Recetas')

    def contar_recetas(ruta):
        return sum(1 for _ in Path(ruta).glob("**/*.txt"))

    def inicio():
        system('cls')
        print('*' * 50)
        print('Bienvenido al Administrador de Recetas')
        print('*' * 50)
        print(f'Las recetas están en {mi_ruta}')
        print(f'Total de recetas: {contar_recetas(mi_ruta)}')
    
    opciones = '''
        [1] - Leer receta
        [2] - Crear receta
        [3] - Crear categoría nueva
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Salir del programa
        '''
        while True:
            print(opciones)
            eleccion = input("Elige una opción: ")
            if eleccion.isdigit() and 1 <= int(eleccion) <= 6:
                return int(eleccion)
              finalizar_programa = False

    while not finalizar_programa:
        opcion = inicio()
        if opcion == 6:
            finalizar_programa = True
        else:
            print(f"Opción {opcion} seleccionada")  # Aquí se llamarán las funciones respectivas.

    print("Gracias por usar el programa.")
