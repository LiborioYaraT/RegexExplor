import re  

# --- Patrones para cada idioma ---

patronesEspañol = {
    "float": r'-?\d+\.\d+',  
    "entero": r'\d+',  
    "string": r'[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+',
    "lista": r':([^.:]*\.)'
}

patronesFrances = {
    "float": r'\d+,\d+',  
    "entero": r'\d+',  
    "string": r'[a-zA-ZàâçéèêëîïôûùüÿæœÁÉÍÓÚÑ]+',
    "lista": r':([^.:]*\.)'
}

patronesItaliano = {
    "float": r'\d+,\d+',  
    "entero": r'\d+',  
    "string": r'[a-zA-ZàèéìíîòóùúÀÈÉÌÍÎÒÓÙÚ]+',
    "lista": r':([^.:]*\.)'
}

# --- Entrada del usuario ---
idioma = input("Elige el idioma del texto (Español(1), Francés(2), Italiano(3)): ").strip()
texto = input("Pega el texto a analizar:\n")

# --- Procesamiento según el idioma ---
if idioma == "1":
    patrones = patronesEspañol
    idioma_nombre = "Español"
elif idioma == "2":
    patrones = patronesFrances
    idioma_nombre = "Francés"
elif idioma == "3":
    patrones = patronesItaliano
    idioma_nombre = "Italiano"
else:
    print("⚠️ Idioma no reconocido. Debe ser: Español(1), Francés(2) o Italiano(3).")
    exit()

# --- Análisis ---
# Detectar floats primero
floats = re.findall(patrones["float"], texto)

# Detectar enteros y excluir los que forman parte de floats
enteros = re.findall(patrones["entero"], texto)
enteros_filtrados = [n for n in enteros if not re.search(rf'{n}[,.]\d+', texto)]

# Strings y listas
strings = re.findall(patrones["string"], texto)
listas = re.findall(patrones["lista"], texto)

# --- Resultados ---
print(f"\n=== Resultados para {idioma_nombre} ===")
print(f"Enteros totales encontrados: {len(enteros_filtrados)}")
print(f"Floats totales encontrados: {len(floats)}")
print(f"Strings totales encontrados: {len(strings)}")
print(f"Listas totales encontradas: {len(listas)}")