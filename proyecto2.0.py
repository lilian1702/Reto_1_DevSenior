#RETO 1 - Proyecto de Investigación Científica en Python

#objetivos Recopilación de datos experimentales
#analisis de resultados experimentales
#generacion de un informe final
#validacion y manejo de errores
#interaccion mediante un meno de opciones

from datetime import datetime
# se crea un lista de experimentos que contiene informacion sobre distintos experimentos a realizar,
#cada elemento de la lista es a su vez una sublista que reperesnta el experimento
#con los datos correspondientes como nombre, fecha, tipo y resultados
listaDeExperimentos = [ 
    ["experimento1", "16/11/2024", "quimica", [5, 4, 3, 2, 1]],
    ["experimento2", "16/11/2024", "Fisica", [8, 9, 10, 11]],
    ["experimento3", "17/11/2024", "Ciencias Naturales", [7, 6, 5, 4, 3]],
    ["experimento4", "18/11/2024", "Biologia", [9, 8, 7, 6, 5]],
]

# se crea la funcion de inicializacion usando el metodo constructor para 
# escrbir parametros que se puedan reescribir varias veces y almacenar diferente informacion
class Experimento:
    def __init__(self, nombre, fechaExperimento, tipo, resultados):
        self.nombre = nombre
        self.fechaExperimento = fechaExperimento
        self.tipo = tipo
        self.resultados = resultados

# se crea la Funcion para agregar un experimento
# la cual perimite crear un objeto y lo agrega a la lista de experimentos
#solicita informacion sobre el experimento y valida los datos ingresados
#y los agrega a la lista
def agregar_experimento(listaDeExperimentos):
    try:
        nombre = input("Ingrese el nombre del experimento: ")
        fechaExperimento_str = input("Ingrese la fecha del experimento (dd/mm/yyyy): ")
        try:
            fechaExperimento = datetime.strptime(fechaExperimento_str, "%d/%m/%Y").strftime("%d/%m/%Y")
        except ValueError:
            print("Error: La fecha ingresada no es válida.")
            return

        tipo = input("Ingrese el tipo de experimento (quimica, Fisica, Biologia, Ciencias Naturales): ")

        resultados = list(map(int, input("Ingrese los resultados numéricos del experimento separados por comas: ").split(",")))

        listaDeExperimentos.append([nombre, fechaExperimento, tipo, resultados])
        print("Experimento agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar el experimento: {e}")
        

#la funcion visualizar experimentos permite como su nombre lo indica
#visualizar en la consola una lista detallada de los experimentos 
#registrados previamente, en caso de no haber experimentos informa al usuario que no
#se encuentra  ningun registro
def visualizar_experimentos(listaDeExperimentos):
    if not listaDeExperimentos:
        print("No hay experimentos registrados. Agregue al menos uno antes de visualizar.")
        return

    print("\nLista de experimentos registrados:")
    for i, experimento in enumerate(listaDeExperimentos, start=1):
        nombre, fecha, tipo, resultados = experimento
        print(f"\nExperimento {i}:")
        print(f"  Nombre: {nombre}")
        print(f"  Fecha: {fecha}")
        print(f"  Tipo: {tipo}")
        print(f"  Resultados: {resultados}")
        
#la funcion eliminar experimento permite como su nombre lo indica
#eliminar un experimento especifico de la lsita basado en su nombre
#y porteriormente se notifica al usuario de que ha sido eleiminado
def eliminar_experimento(listaDeExperimentos):
    nombre = input("Ingrese el nombre del experimento que desea eliminar: ")

    for experimento in listaDeExperimentos:
        if experimento[0] == nombre:
            listaDeExperimentos.remove(experimento)
            print(f"El experimento '{nombre}' ha sido eliminado correctamente.")
            return
    print(f"Error: No se encontró un experimento con el nombre '{nombre}'.")

#esta funcion permite el calculo de estadisticas como promedio, valor maximo, valor minimo
#de los resultados registrados en los experimentos de la lsita
def calcular_estadisticasExperimento(listaDeExperimentos):
    visualizar_experimentos(listaDeExperimentos)
    try:
        index = int(input("Ingrese el número del experimento: ")) - 1
        if 0 <= index < len(listaDeExperimentos):
            resultados = listaDeExperimentos[index][3]
            promedio = sum(resultados) / len(resultados)
            maximo = max(resultados)
            minimo = min(resultados)
            print(f"Estadísticas del experimento {listaDeExperimentos[index][0]}:")
            print(f"  Promedio: {promedio}")
            print(f"  Mínimo: {minimo}")
            print(f"  Máximo: {maximo}")
        else:
            print("Error: Número de experimento inválido.")
    except ValueError:
        print("Error: Entrada inválida.")

#la funcion compara experimentos permite comparar los promedios
#de los experimentos seleccionados, evidenciando los promedios de menor a mayor
def comparar_experimentos(listaDeExperimentos):
    visualizar_experimentos(listaDeExperimentos)
    try:
        indices = list(map(int, input("Ingrese los índices de los experimentos que desea comparar, separados por comas: ").split(",")))
        resultados_comparados = []
        for index in indices:
            if 0 <= index - 1 < len(listaDeExperimentos):
                promedio = sum(listaDeExperimentos[index - 1][3]) / len(listaDeExperimentos[index - 1][3])
                resultados_comparados.append((index - 1, promedio))
            else:
                print(f"Índice {index} es inválido.")
        
        resultados_comparados.sort(key=lambda x: x[1])
        print("\nResultados comparados:")
        for index, promedio in resultados_comparados:
            print(f"{index + 1}. {listaDeExperimentos[index][0]} - Promedio: {promedio}")
    except ValueError:
        print("Error: Entrada inválida.")
# esta funcion genera un archivo de texto que contiene infoormacion
#de los experimentos registrados en la lista
#cada experimento se presenta con datos como nombre, fecha, tipo y resultados
def generar_informe(listaDeExperimentos):
    if not listaDeExperimentos:
        print("No hay experimentos registrados. Agregue al menos uno antes de generar el informe.")
        return

    with open("informe_experimento.txt", "w") as archivo:
        for experimento in listaDeExperimentos:
            archivo.write(f"Nombre: {experimento[0]}\n")
            archivo.write(f"Fecha: {experimento[1]}\n")
            archivo.write(f"Tipo: {experimento[2]}\n")
            archivo.write(f"Resultados: {experimento[3]}\n")
            archivo.write("\n")

    print("Informe generado como 'informe_experimento.txt'.")
#La función mostrar_menu proporciona un menú interactivo 
# para gestionar experimentos y realizar diversas operaciones relacionadas con ellos. 
# Permite al usuario seleccionar opciones para agregar, visualizar, eliminar experimentos, 
# realizar análisis de datos y generar informes. 
# El programa continúa ejecutándose hasta que el usuario elija salir
def mostrar_menu():
    while True:
        print("\n==== Menú Principal ====")
        print("=== Gestión de Experimentos ===")
        print("1. Agregar experimento")
        print("2. Visualizar experimentos")
        print("3. Eliminar experimento")
        print("=== Análisis de Datos ===")
        print("4. Calcular estadísticas")
        print("5. Comparar experimentos")
        print("=== Generar Informe ===")
        print("6. Generar informe")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_experimento(listaDeExperimentos)
        elif opcion == "2":
            visualizar_experimentos(listaDeExperimentos)
        elif opcion == "3":
            eliminar_experimento(listaDeExperimentos)
        elif opcion == "4":
            calcular_estadisticasExperimento(listaDeExperimentos)
        elif opcion == "5":
            comparar_experimentos(listaDeExperimentos)
        elif opcion == "6":
            generar_informe(listaDeExperimentos)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Error: Opción inválida.")

if __name__ == "__main__":
    mostrar_menu()
    
    
