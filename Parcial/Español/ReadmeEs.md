# 📊 Extracción de patrones con expresiones regulares en Python 

Este proyecto utiliza **expresiones regulares (regex)** en Python para identificar diferentes tipos de datos dentro de un texto: números enteros, números decimales (floats), cadenas de texto y listas.

---

## 📌 Descripción

El script toma un texto de ejemplo que contiene números, palabras, símbolos y listas, y luego aplica diferentes **patrones regex** para extraer:

- 🔢 **Enteros:** números sin decimales.  
- 📐 **Floats:** números con decimales.  
- 📝 **Strings:** secuencias de letras (incluye acentos y caracteres especiales en español).  
- 📋 **Listas:** expresiones tipo lista (elementos después de `:` seguidos de un punto).  

El código imprime la cantidad de coincidencias encontradas en cada categoría, incluyendo repetidas.

---

## 🚀 Ejecución

1. Clonar o descargar este archivo.  
2. Ejecutar en la terminal:

```bash
python ParEs.py

📂 Patrones usados

Enteros

(?<![\d,.-])\d+(?!,\d)


Detecta enteros evitando confusión con comas o puntos decimales.

Floats

-?\d+\.\d+


Captura números con decimales positivos o negativos.

Strings

[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+


Reconoce palabras con caracteres del español.

Listas

:([^.:]*\.)


Busca secuencias tipo lista después de : y antes de un punto final.

🔧 Requisitos

Python 3.x

Librería estándar re (incluida por defecto en Python).

📖 Notas

El patrón para booleanos (True, False, true, false) está preparado pero comentado en el código.

Se pueden adaptar o extender los patrones para detectar más tipos de datos.