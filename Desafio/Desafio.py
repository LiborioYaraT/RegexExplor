import re

texto = input("Ingresa el texto a analizar: ")

# Patrones para cada tipo de dato
patrones = {
    'Entero': r'-?\b\d+\b', 
    'Flotante': r'-?\b\d+\.\d+\b',
    'Booleano': r'\b(True|False)\b',
    'String': r'\w[a-zA-Z]+',
    'Lista de números': r'\[[-\d,\s\.]+\]'
}

# Buscar todas las coincidencias
resultados = []
for tipo, patron in patrones.items():
    coincidencias = re.findall(patron, texto)
    for coincidencia in coincidencias:
        resultados.append((coincidencia, tipo))

print("\nResultados del análisis:")
print("-" * 40)
if resultados:
    for coincidencia, tipo in resultados:
        print(f"'{coincidencia}' -> {tipo}")
else:
    print("No se encontraron coincidencias.")