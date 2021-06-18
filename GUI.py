#!/usr/bin/env python
# -*- coding: utf-8 -*-  
from nltk import TweetTokenizer
from tabulate import tabulate
import json
import requests
from Tkinter import *
import sys
import codecs


sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

root=Tk()
textBox=Text(root, height=5, width=28)
url = 'http://127.0.0.1:5080/postagging/'

#Se insurrecciona el pueblo de la gente de Arabia contra el golpe de estado. En el fondo del conflicto se mueven intensas luchas por el agua en un pais que se desertiza y padece hambre.
#Madre de el detenido #Assange manda mensaje a @Lenin: Que el rostro de mi sufrido hijo persiga tus noches de insomnio
#@Serpiente estoy muy emocionado con el estreno de #AvengersEndgame. No puedo esperar!
#@Carol123 Con motivo de lo nuevo de Marvel, un hilo:
#@petrogustavo Se autodenomina liberal cuando esta destruyendo la Justicia y la verdad
#Navarro y Mockus, dos bajas personales que son una verdadera perdida para Colombia.

def retrieve_input():
    string_value = textBox.get("1.0","end-1c")
    tweet = str(string_value).decode('utf-8')
    display_categories(tweet)

def clear_text():
    textBox.delete("1.0","end-1c")
    
def retrive_tknzr(tweet_string):
    tweet_tokenizer = TweetTokenizer()
    tknzr = tweet_tokenizer.tokenize(tweet_string)
    display_tknzr = [item.encode('utf-8') for item in tknzr]
    return display_tknzr

def retrieve_info(tweet_string):
    dictionary = { i+1 : retrive_tknzr(tweet_string)[i] for i in range(0, len(retrive_tknzr(tweet_string)))}
    postag_structure = {'texto': json.dumps(dictionary)}
    response = requests.post(url, data=json.dumps(postag_structure), headers={"Content-Type": "application/json"})
    result = json.loads(response.json()['texto']) #Loads JSON data from String
    return result

def retrieve_data(tweet_string):
    display_data = json.dumps(retrieve_info(tweet_string), indent=2, ensure_ascii=False).encode('utf-8') #Outputs a String in proper JSON data
    return display_data

#Not very elegant or short but it works
def retrieve_category(argument):
    i=0
    category = ""
    if argument[0] == "V":
        category = "Verbo "
        i = i + 1                                               
        for i in range(len(argument)):
            if argument[i] == "M" and i == 1:
                category += "Principal "
            elif argument[i] == "A" and i == 1:
                category += "Auxiliar "
            elif argument[i] == "I" and i == 2:
                category += "Indicativo "
            elif argument[i] == "S" and i == 2:
                category += "Subjuntivo "
            elif argument[i] == "M" and i == 2:
                category += "Imperativo "
            elif argument[i] == "C" and i == 2:
                category += "Condicional "
            elif argument[i] == "N" and i == 2:
                category += "Infinitivo "
            elif argument[i] == "G" and i == 2:
                category += "Gerundio " 
            elif argument[i] == "P" and i == 2:
                category += "Participio "
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
        for i in range(len(argument)):
            if argument[i] == "Q" and i == 1:
                category += "Calificativo "
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
        for i in range(len(argument)):
            if argument[i] == "G":
                category += "General" 
    if argument[0] == "D":
        category = "Determinante "
        i = i + 1
        for i in range(len(argument)):
            if argument[i] == "D" and i == 1:
                category += "Demostrativo "
            elif argument[i] == "P" and i == 1:
                category += "Posesivo "
            elif argument[i] == "T" and i == 1:
                category += "Interrogativo "
            elif argument[i] == "E" and i == 1:
                category += "Exclamativo "
            elif argument[i] == "I" and i == 1:
                category += "Indefinido "
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
        for i in range(len(argument)):
            if argument[i] == "P" and i == 1:
                category += "Personal "
            elif argument[i] == "D" and i == 1:
                category += "Demostrativo "
            elif argument[i] == "X" and i == 1:
                category += "Posesivo "
            elif argument[i] == "I" and i == 1:
                category += "Indefinido "    
            elif argument[i] == "T" and i == 1:
                category += "Interrogativo "
            elif argument[i] == "R" and i == 1:
                category += "Relativo "
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
        for i in range(len(argument)):
            if argument[i] == "C" and i == 1:
                category += "Comun "
            elif argument[i] == "P" and i == 1:
                category += "Propio "    
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
        for i in range(len(argument)):
            if argument[i] == "C" and i == 1:
                category += "Coordinada "
            elif argument[i] == "S":
                category += "Subordinada "
    if argument[0] == "I":
        category = "Interjeccion"
    if argument[0] == "F":
        category = "Signo de Puntuacion"
    if argument[0] == "S":
        category = "Adposicion "
        i = i + 1
        for i in range(len(argument)):
            if argument[i] == "P":
                category += "Preposicion "
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
    return category

#Shows every category found on a given text
def display_categories(tweet_string):
    json_object = retrieve_info(tweet_string)
    lema = []
    eagles = []
    categoria = []
    inicio = """<!DOCTYPE html><html><head><title>PLN</title><link rel="stylesheet" href="styles.css"></head>"""
    final = """</html>"""
    for words in range(0, len(retrive_tknzr(tweet_string))): #Amount of words on a text
        for categories in range(0, len(json_object[words]['lemas'])): #Amount of categories and lemas
            lema.append(json_object[words]['lemas'][categories]['lema'])
            eagles.append(json_object[words]['lemas'][categories]['categoria'])
            categoria.append(retrieve_category(json_object[words]['lemas'][categories]['categoria']))
    table = zip(lema, eagles, categoria)
    html_file = open('salida.html', 'w')
    message = tabulate(table, headers=['Lema', 'EAGLES', 'Categoria'], tablefmt='html').decode('utf-8', 'ignore')
    html_file.write(inicio)
    html_file.write(message)
    html_file.write(final)
    html_file.close()

ingrese_texto = Label(root, text= str("Ingrese su texto aquí"))
ingrese_texto.pack()
textBox.pack()
root.geometry('200x125')
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
#root.resizable(False, False)
root.title("PLN Project")
buttonCancel = Button(root, height=1, width=11, padx=5, pady=5, text="Cancelar", command=lambda: clear_text())
buttonCancel.pack(side = LEFT)
buttonCommit=Button(root, height=1, width=11, padx=5, pady=5, text="Aceptar", command=lambda: retrieve_input())
buttonCommit.pack(side = LEFT)
mainloop()