import random

# -----------------------------
# LISTA DE PREGUNTAS
# -----------------------------

Preguntas = [
    ("¿Cuál es la capital de Francia?", "París", "Madrid", "Roma"),
    ("¿Cuánto es 3 x 4?", "12", "9", "14"),
    ("¿Qué lenguaje estamos usando?", "Python", "Java", "C++"),
    ("¿Cuál es el planeta más cercano al Sol?", "Mercurio", "Venus", "Marte"),
    ("¿Qué color resulta de mezclar azul y amarillo?", "Verde", "Rojo", "Naranja")
    ]

# -----------------------------
# LISTA PARA GUARDAR RESULTADOS
# -----------------------------
# Cada elemento será una tupla: (aciertos, errores, porcentaje)

Resultados = []

# -----------------------------
# FUNCIONES
# -----------------------------

def menu_principal():
    """
    Muestra el menú principal y gestiona la interacción del usuario.
    Permite:
    1 - Jugar una partida de trivia
    2 - Ver resultados de partidas anteriores
    3 - Salir del programa
    """

    opcion = ""
    while opcion != "3":  # Centinela = '3' para salir
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Jugar trivia")
        print("2. Mostrar resultados")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            jugar_trivia()
        elif opcion == "2":
            mostrar_resultados()
        elif opcion == "3":
            print("¡Gracias por jugar! Hasta pronto.")
        else:
            print("Opción inválida. Intenta de nuevo.")

def jugar_trivia():
    """
    Ejecuta una partida de trivia:
    - Recorre todas las preguntas
    - Mezcla y muestra las opciones
    - Cuenta aciertos y errores
    - Calcula porcentaje
    - Si porcentaje < 50%, permite volver a jugar (recursividad)
    - Guarda los resultados en la lista `resultados`
    """
    random.shuffle(Preguntas)  # Mezcla el orden de las preguntas
    aciertos = 0
    errores = 0

    for p in Preguntas:
        if mostrar_pregunta(p):
            aciertos += 1
        else:
            errores += 1

    total = aciertos + errores
    porcentaje = calcular_porcentaje(aciertos, total)

    print(f"\nAciertos: {aciertos}")
    print(f"Errores: {errores}")
    print(f"Porcentaje de aciertos: {porcentaje:.2f}%")

    Resultados.append((aciertos, errores, porcentaje))  # Guarda la partida

    # Si menos del 50%, volver a jugar usando recursividad
    if porcentaje < 50:
        print("\nNo alcanzaste el 50%. ¡Vuelve a intentarlo!\n")
        jugar_trivia()  # Llamada recursiva

def mostrar_pregunta(p):
    """
    Recibe una tupla con (enunciado, lista_opciones, respuesta_correcta).
    Muestra la pregunta y sus opciones mezcladas.
    Devuelve True si el usuario acierta, False si se equivoca.
    """

def calcular_porcentaje(aciertos, total):
    """
    Calcula el porcentaje de aciertos sobre el total de preguntas.
    """
    return (aciertos / total) * 100

def mostrar_resultados():
    """
    Muestra todas las partidas jugadas y estadísticas generales:
    - Listado de resultados
    - Máximo, mínimo y promedio de aciertos
    """

# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------

menu_principal()