# 📊 Extracción de patrones con expresiones regulares en Python (Texto en italiano)

Este proyecto utiliza **expresiones regulares (regex)** en Python para identificar diferentes tipos de datos dentro de un texto en **italiano**: números enteros, números decimales (con coma), cadenas de texto y listas.

---

## 📌 Descripción

El script toma un texto de ejemplo en italiano que contiene números, palabras, símbolos y listas, y luego aplica diferentes **patrones regex** para extraer:

- 🔢 **Enteros:** números sin decimales.  
- 📐 **Floats:** números con coma como separador decimal (formato italiano, ej: `95,90`).  
- 📝 **Strings:** secuencias de letras (incluye caracteres acentuados en italiano).  
- 📋 **Listas:** expresiones tipo lista (elementos después de `:` seguidos de un punto).  

El código imprime la cantidad de coincidencias encontradas en cada categoría.

---

## 🚀 Ejecución

1. Clonar o descargar este archivo.  
2. Ejecutar en la terminal:

```bash
python ParIta.py

📂 Patrones usados

Enteros

\d+


Detecta números enteros. Se filtran aquellos que forman parte de decimales (con coma).

Floats

\d+,\d+


Captura números con coma decimal (estilo italiano).

Strings

[a-zA-ZàèéìíîòóùúÀÈÉÌÍÎÒÓÙÚ]+


Reconoce palabras con caracteres del alfabeto italiano y vocales acentuadas.

Listas

:([^.:]*\.)


Busca secuencias tipo lista después de : y antes de un punto final.

🔧 Requisitos

Python 3.x

Librería estándar re (incluida por defecto en Python).

📖 Notas

Los decimales se consideran con coma , en lugar de punto ., siguiendo la convención italiana.

El patrón de strings está adaptado para acentos y caracteres especiales en italiano.

Se pueden extender los patrones para soportar más casos o lenguajes.