import re

texto = """En el año 2025, 25 maestros enseñan juntos. ¡Hola! ¿Te gusta aprender? El cielo educativo, las estrellas (★) brillan. 21 niños estudian, 20.25 horas de clase. Lista: libro, pizarra, marcador. El costo es $100.10. ¿Sabías que el código #5566 es especial? La vida es enseñanza, @todos participan. El tiempo avanza, 22 días de aprendizaje. ¡Enseña! El número especial es 1515. ¿Qué harías con 63.60 pesos? La respuesta está en la lista: leer, explicar, compartir. ¡Aprende siempre! 100 palabras, 22 enteros, 3 decimales, 2 listas."""

patron_entero = r'(?<![\d,.-])\d+(?!,\d)'

coincidencias = re.findall(patron_entero, texto)
unicos = set(coincidencias)

#print(f"Enteros únicos encontrados: {len(unicos)}")
print(f"Enteros totales encontrados (incluyendo repetidos): {len(coincidencias)}")
#print("Únicos:", list(unicos))

patron_float = r'-?\d+\.\d+'

coincidencias = re.findall(patron_float, texto)
unicos = set(coincidencias)

#print(f"Floats únicos encontrados: {len(unicos)}")
print(f"Floats totales encontrados (incluyendo repetidos): {len(coincidencias)}")
#print("únicos:", list(unicos)[:5])

patron_booleano = r'\b(True|False|true|false)\b'

#coincidencias = re.findall(patron_booleano, texto)
#unicos = set(coincidencias)

#print(f"Booleanos únicos encontrados: {len(unicos)}")
#print(f"Booleanos totales encontrados (incluyendo repetidos): {len(coincidencias)}")
#print("Únicos:", list(unicos))

patron_string = r'[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+'

coincidencias = re.findall(patron_string, texto)
unicos = set(coincidencias)

#print(f"Strings únicos encontrados: {len(unicos)}")
print(f"Strings totales encontrados (incluyendo repetidos): {len(coincidencias)}")
#print("Únicos:", list(unicos)[:5])

#patron_lista = r'\[(?:\s*-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?\s*,)*\s*(?:-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|\.\.\.)\s*\]'

patron_lista = r':([^.:]*\.)'


coincidencias = re.findall(patron_lista, texto)
unicos = set(coincidencias)

#print(f"Listas de números únicas encontradas: {len(unicos)}")
print(f"Listas de números totales encontradas (incluyendo repetidas): {len(coincidencias)}")
#print("Úicoss:", list(unicos)[:5])