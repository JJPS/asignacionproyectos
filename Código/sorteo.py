# Herramienta para asignación aleatoria de proyectos y alumnos
# 10 de Noviembre 2022

# Importar librerias
import sys
import random
from tabulate import tabulate
import time
import os

# Funciones auxiliares
def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

# Declaración variables
proyectos = ["Gestion FCT", "Evaluación inicial Alumnos","Terraza Cafetería","Taller vehículos", "Recetas cocina","Mantenimiento Industrial", "Pujas","Tienda OnLine", "Gestión de Almacen", "Gestión de Payloads", "Biblioteca Escolar"]
alumnos = ["Arqués, Manuel", "Ben Allal, Zakarias","Carmona,Miguel A.", "Lázaro, Maria Belén","Mimun, Yunes","Mohamed, Sufian","Navarro, Alejandro", "Soria, José Luis","Torreblanca, Alejandro","Valenzuela, Álvaro","Zamudio, José Ramón"]

# Comprobar que proyectos >= alumnos
if len(proyectos)<len(alumnos):
    print("Los proyectos asignados son insuficientes, agregue "+str(len(alumnos)-len(proyectos))+" proyecto/s")
    sys.exit()

# Desordenar listas

random.shuffle(proyectos)
random.shuffle(alumnos)

# Generar lista
listado = []
n=0
for alum in alumnos:
    linea = []
    linea.append(alum)
    linea.append(proyectos[n])
    n=n+1
    listado.append(linea)
listado  = sorted(listado)

# Mostrar lista
borrarPantalla
print("")
print(tabulate (listado,headers=["Alumno","Proyecto"]))
print("")
print ("Sorteo generado el "+time.strftime("%c"))
print("")


