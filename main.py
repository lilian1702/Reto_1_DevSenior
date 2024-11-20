import datetime

listaDeExperimentos = [
    ["experimento1", "16/11/2024","quimica", [5,4,3,2,1]],
    ["experimento2", "16/11/2024","Fisica", [8,9,10,11]],
    ["experimento3", "17/11/2024","Ciencias Naturales", [7,6,5,4,3]],
    ["experimento4", "18/11/2024","Biologia", [9,8,7,6,5]],
]

class Experimentos:
    def __init__(self, nombre, fechaExperimento, tipo, resultados):
        self.nombre = nombre
        self.fechaExperimento = fechaExperimento
        self.tipo = tipo
        self.resultados = resultados
        

def agregar_experimento():
    nombre= input ("ingrese el nombre del experimento")
    fechaExperimento_str= input ("ingrese la fecha del experimento")
    try:
        fechaExperimento = datetime.strptime(fechaExperimento_str, "%d/%m/%Y")
    
    except ValueError:
        print("Error: la fecha ingresada no es valida.")
        return
  
    tipo= input("ingrese el tipo de experimento(quimica, Fisica, Biologia, Ciencias Naturales):") 
  
    resultados= input("ingrese los resultados numericos del experimento")
              
    experimento= Experimentos(nombre,fechaExperimento, tipo, resultados)
    
    listaDeExperimentos.append([nombre,fechaExperimento_str,tipo,resultados])
    print("Experimento agregado correctamente")
    # permite agregar experimentos con sus nuevos atributos
    pass

def eliminar_experimeintos():
    #permite eliminar un experimento
    #dificultad 1: requiere la funcion agregar experimento
    pass

def visualizar_experimentos():
    #perimite visualizar todos los experimentos
    #requiere el uso de la funcion agregar experimeinto. dificultad 1
    pass

def calcular_estadisticas():
    # calcular estadisticas basicas (promedios, maximos y minimos de un experimento)
   #dificultad 2. requiere el uso de funciones agregar_experimeentos
    
    pass

def compara_experimentos():
    #compara dos o mas experimentos para determinar los mejores o peores resultados
    #dificultad 3, requiere el uso de funciones calcular_funciones
    pass

def generar_informe():
    #gererar un infoeme resumen de los experimentos y sus estadisticas. difiultad 3
    #requiere el suso de funciones visualizar_experimentos y calcular_estadisticas
    pass

def mostrar_menu():
    #muestra el menu principal del programa. difiultad 1
    print("====menu principal=====")
    print("===gestios de experimentos===")
    print("1. Agregar experimento")
    print("2. Visualizar experimentos")
    print("3. eliminar experimentos")
    print("====analisis de datos=====")
    print("4.calcular estadisticas")
    print("5. comparar experimentos")
    print("====generar informe=====")
    print("===salir===")
    print("Ingrese una opcion:")
    print ("7. salir")


def main():
    #esta funcion controla el flujo general del sistema
    pass
main()



