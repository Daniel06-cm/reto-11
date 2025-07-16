import re
from collections import Counter

def analizar_mbox():
    # Ruta fija al archivo
    ruta_archivo =  r"C:\Users\danie\Downloads\mbox.txt"


    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read().lower()

    # Contar vocales
    vocales = 'aeiou'
    cantidad_vocales = sum(texto.count(v) for v in vocales)

    # Contar consonantes
    consonantes = 'bcdfghjklmnpqrstvwxyz'
    cantidad_consonantes = sum(texto.count(c) for c in consonantes)

    # Extraer palabras con solo letras (sin números ni símbolos)
    palabras = re.findall(r'\b[a-z]+\b', texto)

    # Contar las 50 palabras más frecuentes
    top_50 = Counter(palabras).most_common(50)

    # Mostrar resultados
    print(" Análisis de archivo mbox.txt")
    print(f" Cantidad de vocales: {cantidad_vocales}")
    print(f" Cantidad de consonantes: {cantidad_consonantes}")
    print("\n Top 50 palabras más frecuentes:")
    for palabra, frecuencia in top_50:
        print(f"{palabra}: {frecuencia}")

# Ejecutar el análisis directamente
analizar_mbox()
