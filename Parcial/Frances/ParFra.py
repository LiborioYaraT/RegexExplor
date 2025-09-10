import re 

texto = """Bonjour! En 2025, 23 professeurs enseignent ensemble. Liste: livre, tableau, marqueur. Le prix est de 98,30€. Les étoiles (★) brillent la nuit. 19 chats étudient, 18 chiens expliquent. Le code #7788 est spécial. 22 jours d'apprentissage, 16 jours de repos. @tous enseignent. Le numéro magique est 1525. Que feriez-vous avec 66,80€? La réponse est dans la liste: lire, expliquer, partager. Apprenez toujours! 100 mots, 22 entiers, 3 decimales, 2 listas."""

patron_entero = r'\d+'  
coincidencias = re.findall(patron_entero, texto)
coincidencias = [n for n in coincidencias if not re.search(rf'{n},\d+', texto)]
print(f"Enteros totales encontrados (incluyendo repetidos): {len(coincidencias)}")

patron_float = r'\d+,\d+'  
coincidencias = re.findall(patron_float, texto)
print(f"Floats totales encontrados (incluyendo repetidos): {len(coincidencias)}")

patron_string = r'[a-zA-ZàâçéèêëîïôûùüÿñæœÁÉÍÓÚÑ]+'
coincidencias = re.findall(patron_string, texto)
print(f"Strings totales encontrados (incluyendo repetidos): {len(coincidencias)}")

patron_lista = r':([^.:]*\.)'
coincidencias = re.findall(patron_lista, texto)
print(f"Listas totales encontradas (incluyendo repetidas): {len(coincidencias)}")