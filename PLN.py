#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from nltk import TweetTokenizer
from tabulate import tabulate
import json
import requests
import sys
import codecs


sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

cat = []
tipo = []
modo = []
tiempo = []

url = 'http://127.0.0.1:5080/postagging/'
tweet = str("Fingir").decode('utf-8')
tweet_tokenizer = TweetTokenizer()

#Not very elegant or short but it works
def retrieve_category(argument):
    i=0
    category = ""
    if argument[0] == "V":
        category = "Verbo "
        cat.append(category)
        i = i + 1                                               
        for i in range(len(argument)):
            if argument[i] == "M" and i == 1:
                category += "Principal "
                tipo.append("Principal")
            elif argument[i] == "A" and i == 1:
                category += "Auxiliar "
                tipo.append("Auxiliar")
            elif argument[i] == "I" and i == 2:
                category += "Indicativo "
                tipo.append("No")
            elif argument[i] == "S" and i == 2:
                category += "Subjuntivo "
                tipo.append("No")
            elif argument[i] == "M" and i == 2:
                category += "Imperativo "
                tipo.append("No")
            elif argument[i] == "C" and i == 2:
                category += "Condicional "
                tipo.append("No")
            elif argument[i] == "N" and i == 2:
                category += "Infinitivo "
                tipo.append("No")
            elif argument[i] == "G" and i == 2:
                category += "Gerundio "
                tipo.append("No") 
            elif argument[i] == "P" and i == 2:
                category += "Participio "
                tipo.append("No")
            elif argument[i] == "P" and i == 3:
                category += "Tiempo Presente "
            elif argument[i] == "I" and i == 3:
                category += "Tiempo Imperfecto "
            elif argument[i] == "F" and i == 3:
                category += "Tiempo Futuro "
            elif argument[i] == "S" and i == 3:
                category += "Tiempo Pasado "
            elif argument[i] == "1" and i == 4:
                category += "Primera Persona "
            elif argument[i] == "2" and i == 4:
                category += "Segunda Persona "                                                                   
            elif argument[i] == "3" and i == 4:
                category += "Tercera Persona "
            elif argument[i] == "S" and i == 5:
                category += "Singular"
            elif argument[i] == "P" and i == 5:
                category += "Plural"   
            elif argument[i] == "M" and i == 5:
                category += "Masculino"
            elif argument[i] == "F" and i == 5:
                category += "Femenino"             
    if argument[0] == "A":
        category = "Adjetivo "
        i = i + 1
        cat.append(category)
        for i in range(len(argument)):
            if argument[i] == "Q" and i == 1:
                category += "Calificativo "
                tipo.append("Calificativo")
            elif argument[i] == "A" and i == 2:
                category += "Apreciativo "
            elif argument[i] == "M" and i == 3:
                category += "Masculino "
            elif argument[i] == "F" and i == 3:
                category += "Femenino "
            elif argument[i] == "C" and i == 3:
                category += "Comun "
            elif argument[i] == "S" and i == 4:
                category += "Singular "
            elif argument[i] == "P" and i == 4:
                category += "Plural "
            elif argument[i] == "N" and i == 4:
                category += "Invariable " 
            elif argument[i] == "P" and i == 6:
                category += "Participio "   
    if argument[0] == "R":
        category = "Adverbio "
        i = i + 1
        cat.append(category)
        for i in range(len(argument)):
            if argument[i] == "G":
                category += "General"
                tipo.append("General") 
    if argument[0] == "D":
        category = "Determinante "
        i = i + 1
        cat.append(category)
        for i in range(len(argument)):
            if argument[i] == "D" and i == 1:
                category += "Demostrativo "
                tipo.append("Demostrativo")
            elif argument[i] == "P" and i == 1:
                category += "Posesivo "
                tipo.append("Posesivo")
            elif argument[i] == "T" and i == 1:
                category += "Interrogativo "
                tipo.append("Interrogativo")
            elif argument[i] == "E" and i == 1:
                category += "Exclamativo "
                tipo.append("Exclamativo")
            elif argument[i] == "I" and i == 1:
                category += "Indefinido "
                tipo.append("Indefinido")
            elif argument[i] == "1" and i == 2:
                category += "Primera Persona "
            elif argument[i] == "2" and i == 2:
                category += "Segunda Persona "                                                                   
            elif argument[i] == "3" and i == 2:
                category += "Tercera Persona "
            elif argument[i] == "M" and i == 3:
                category += "Masculino "
            elif argument[i] == "F" and i == 3:
                category += "Femenino "
            elif argument[i] == "C" and i == 3:
                category += "Comun "        
            elif argument[i] == "S" and i == 4:
                category += "Singular "
            elif argument[i] == "P" and i == 4:
                category += "Plural "
            elif argument[i] == "N" and i == 4:
                category += "Invariable " 
            elif argument[i] == "1" and i == 6:
                category += "1ra persona-sg "
            elif argument[i] == "2" and i == 6:
                category += "2da persona-sg "
            elif argument[i] == "0" and i == 6:
                category += "3ra persona "
            elif argument[i] == "4" and i == 6:
                category += "1ra persona-pl "
            elif argument[i] == "5" and i == 6:
                category += "2da persona-pl " 
    if argument[0] == "P":
        category = "Pronombre "
        i = i + 1
        cat.append(category)
        for i in range(len(argument)):
            if argument[i] == "P" and i == 1:
                category += "Personal "
                tipo.append("Personal")
            elif argument[i] == "D" and i == 1:
                category += "Demostrativo "
                tipo.append("Demostrativo")
            elif argument[i] == "X" and i == 1:
                category += "Posesivo "
                tipo.append("Posesivo")
            elif argument[i] == "I" and i == 1:
                category += "Indefinido "  
                tipo.append("Indefinido") 
            elif argument[i] == "T" and i == 1:
                category += "Interrogativo "
                tipo.append("Interrogativo") 
            elif argument[i] == "R" and i == 1:
                category += "Relativo "
                tipo.append("Relativo")
            elif argument[i] == "1" and i == 2:
                category += "Primera Persona "
            elif argument[i] == "2" and i == 2:
                category += "Segunda Persona "                                                                   
            elif argument[i] == "3" and i == 2:
                category += "Tercera Persona "
            elif argument[i] == "M" and i == 3:
                category += "Masculino "
            elif argument[i] == "F" and i == 3:
                category += "Femenino "
            elif argument[i] == "C" and i == 3:
                category += "Comun "        
            elif argument[i] == "S" and i == 4:
                category += "Singular "
            elif argument[i] == "P" and i == 4:
                category += "Plural "
            elif argument[i] == "N" and i == 4:
                category += "Invariable "
            elif argument[i] == "N" and i == 5:
                category += "Nominativo "
            elif argument[i] == "A" and i == 5:
                category += "Acusativo "
            elif argument[i] == "D" and i == 5:
                category += "Dativo "
            elif argument[i] == "O" and i == 5:
                category += "Oblicuo "                    
            elif argument[i] == "1" and i == 6:
                category += "1ra persona-sg "
            elif argument[i] == "2" and i == 6:
                category += "2da persona-sg "
            elif argument[i] == "0" and i == 6:
                category += "3ra persona "
            elif argument[i] == "4" and i == 6:
                category += "1ra persona-pl "
            elif argument[i] == "5" and i == 6:
                category += "2da persona-pl "
            elif argument[i] == "P" and i == 7:
                category += "Formal "     
    if argument[0] == "N":
        category = "Nombre "
        i = i + 1
        cat.append(category)
        for i in range(len(argument)):
            if argument[i] == "C" and i == 1:
                category += "Comun "
                tipo.append("Comun")
            elif argument[i] == "P" and i == 1:
                category += "Propio "  
                tipo.append("Propio")  
            elif argument[i] == "M" and i == 2:
                category += "Masculino "
            elif argument[i] == "F" and i == 2:
                category += "Femenino "
            elif argument[i] == "C" and i == 2:
                category += "Comun "
            elif argument[i] == "S" and i == 3:
                category += "Singular "
            elif argument[i] == "P" and i == 3:
                category += "Plural "
            elif argument[i] == "N" and i == 3:
                category += "Invariable "
            elif argument[i] == "A" and i == 6:
                category += "Apreciativo "    
    if argument[0] == "C":
        category = "Conjuncion "
        i = i + 1
        cat.append(category)
        for i in range(len(argument)):
            if argument[i] == "C" and i == 1:
                category += "Coordinada "
                tipo.append("Coordinada")
            elif argument[i] == "S":
                category += "Subordinada "
                tipo.append("Subordinada")
    if argument[0] == "I":
        category = "Interjeccion"
        cat.append(category)
        tipo.append("No")
    if argument[0] == "F":
        category = "Signo de Puntuacion"
        cat.append(category)
        tipo.append("No")
    if argument[0] == "S":
        category = "Adposicion "
        i = i + 1
        cat.append(category)
        for i in range(len(argument)):
            if argument[i] == "P":
                category += "Preposicion "
                tipo.append("Preposicion")
            elif argument[i] == "S" and i == 2:
                category += "Simple " 
            elif argument[i] == "C":
                category += "Contraida "
            elif argument[i] == "M":
                category += "Masculino "
            elif argument[i] == "S" and i == 3:
                category += "Singular "                  
    if argument[0] == "Z":
        category = "Numero" 
        cat.append(category)
        tipo.append("No")
    return category

# Shows every category found on a given text
def display_categories(json_object):
    lema = []
    eagles = []
    categoria = []
    inicio = """<!DOCTYPE html><html><head><title>PLN</title><link rel="stylesheet" href="styles.css"></head>"""
    final = """</html>"""
    for words in range(len(display_tknzr)): #Amount of words on a text
        for categories in range(len(json_object[words]['lemas'])): #Amount of categories and lemas
            lema.append(json_object[words]['lemas'][categories]['lema'])
            eagles.append(json_object[words]['lemas'][categories]['categoria'])
            categoria.append(retrieve_category(json_object[words]['lemas'][categories]['categoria']))
    table = zip(lema, eagles, categoria, tipo)
    html_file = open('salida.html', 'w')
    message = tabulate(table, headers=['Lema', 'EAGLES', 'Categoria', 'Tipo', 'Modo', 'Tiempo', 'Grado', 'Genero', 'Numero', 'Persona', 'Caso', 'Funcion', 'Poseedor'], tablefmt='html').decode('utf-8', 'ignore')
    html_file.write(inicio)
    html_file.write(message)
    html_file.write(final)
    html_file.close()

display_tknzr = [item.encode('utf-8') for item in tweet_tokenizer.tokenize(tweet)]
dictionary = { i+1 : display_tknzr[i] for i in range(0, len(display_tknzr))}
postag_structure = {'texto': json.dumps(dictionary)}
response = requests.post(url, data=json.dumps(postag_structure), headers={"Content-Type": "application/json"})
result = json.loads(response.json()['texto']) #Loads JSON data from String
display_data = json.dumps(result, indent=2, ensure_ascii=False).encode('utf-8') #Outputs a String in proper JSON data
display_categories(result)