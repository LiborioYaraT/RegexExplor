📊 Extracción de patrones con expresiones regulares en Python (Español, Francés e Italiano)

Este proyecto utiliza expresiones regulares (regex) en Python para identificar diferentes tipos de datos dentro de un texto en Español, Francés o Italiano: números enteros, números decimales, cadenas de texto y listas.

📌 Descripción

El script permite al usuario elegir un idioma (Español, Francés o Italiano) y pegar un texto para analizar.
Luego aplica diferentes patrones regex para extraer:

🔢 Enteros: números sin decimales.

📐 Floats: números con punto decimal (Español) o coma decimal (Francés e Italiano).

📝 Strings: secuencias de letras válidas en cada idioma (con sus acentos y caracteres especiales).

📋 Listas: expresiones tipo lista (elementos después de : seguidos de un punto).

El código imprime la cantidad de coincidencias encontradas en cada categoría, incluyendo repetidas.

🚀 Ejecución

Guardar el archivo como Par.py.

Ejecutar en la terminal:

python Par.py


Seleccionar el idioma escribiendo el número correspondiente:

Elige el idioma del texto (Español(1), Francés(2), Italiano(3)):


Pegar el texto que se desea analizar.

📂 Patrones usados
Español

Enteros:

\d+


Detecta números enteros (se filtran los que forman parte de decimales).

Floats:

-?\d+\.\d+


Captura números con punto decimal (ej: 98.30).

Strings:

[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+


Reconoce palabras con caracteres del alfabeto español.

Listas:

:([^.:]*\.)


Busca secuencias tipo lista después de : y antes de un punto.

Francés

Enteros:

\d+


Floats:

\d+,\d+


Captura números con coma decimal (ej: 98,30).

Strings:

[a-zA-ZàâçéèêëîïôûùüÿæœÁÉÍÓÚÑ]+


Reconoce palabras con caracteres franceses (ç, é, à, œ, etc.).

Listas:

:([^.:]*\.)

Italiano

Enteros:

\d+


Floats:

\d+,\d+


Captura números con coma decimal (ej: 95,90).

Strings:

[a-zA-ZàèéìíîòóùúÀÈÉÌÍÎÒÓÙÚ]+


Reconoce palabras con caracteres italianos (ò, ì, ù, etc.).

Listas:

:([^.:]*\.)

🔧 Requisitos

Python 3.x

Librería estándar re (incluida por defecto en Python).

📖 Notas

En Español los floats se escriben con punto (.).

En Francés e Italiano los floats se escriben con coma (,).

Los enteros que forman parte de un número decimal no se cuentan como enteros.

El patrón de strings está adaptado para acentos y caracteres especiales de cada idioma.