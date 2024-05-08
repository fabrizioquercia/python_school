from flask import Flask
from flask_cors import CORS
import functions as FN


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    menu = menu_navigazione()
    return menu + " "+ "Hello, World!"

@app.route("/saluto1")
def saluto1():
    menu = menu_navigazione()
    return menu + " "+ "Ciao abbelli! Questo è il saluto 1!"

@app.route("/saluto2")
def saluto2():
    menu = menu_navigazione()
    return menu + " "+ "Il saluto 2 e' qui e dice: AJOO!"

@app.route("/saluto3")
def saluto3():
    menu = menu_navigazione()
    return menu + " "+ "Saluto 3 e' meglio di me e di te!"

@app.route("/libri")
def libri():
    menu = menu_navigazione()
    html = lista_libri()
    return menu + " "+ html

@app.route("/libri/<id>")
def libro(id):
    menu = menu_navigazione()
    html = lista_libri(id)
    return menu + " "+ html

@app.route("/saluto<i>_bis")
def saluto_bis(i):
    menu = menu_navigazione()
    saluto = ""
    if i== "1": saluto = "Ciao abbelli! Questo è il saluto 1_BIS!"
    if i== "2": saluto = "Il saluto 2_BIS e' qui e dice: AJOO!"
    if i== "3": saluto = "Saluto 3_BIS e' meglio di me e di te!"
    return  menu + " "+  saluto

@app.route("/testo/<t>")
def testo(t):
    testo =""
    if t == "m": testo = FN.media()
    if t == "f": testo = FN.fattoriale()
    if t == "p": testo = FN.potenza()
    return testo


'''
#funzioni interne per def testo()
def media():
    lista = [39, 22, 12,3,5]
    somma = 0
    for i in lista:
        somma += i
    media = somma / len(lista)
    stringa = "La media fra i numeri " + str(lista) + " e' " + str(media) + " - La somma e': " + str(somma)
    return str(stringa)

def fattoriale():
    # Calcolo il fattoriale col ciclo for
    numero = 7
    fattorialeFor = 1
    for i in range(1, numero+1):
        fattorialeFor *= i
    stringa = "Il fattoriale del numero " + str(numero) + " ( " + str(numero) +"! ) e': " + str(fattorialeFor)
    return stringa
    
def potenza():
    numero = 147
    potenza = numero **2
    stringa = "Il numero " + str(numero) + " elevato a potenza e' " + str(potenza)
    return stringa
'''



def menu_navigazione():
    html = "<strong>Saluti standard:</strong><br /><a href='/saluto1'>Saluto 1</a>&nbsp;-&nbsp;<a href='/saluto2'>Saluto 2</a>&nbsp;-&nbsp;<a href='/saluto3'>Saluto 3</a><br />"
    html += "<br /><strong>Saluti BIS:</strong><br /><a href='/saluto1_bis'>Saluto 1 BIS</a>&nbsp;-&nbsp;<a href='/saluto2_bis'>Saluto 2 BIS</a>&nbsp;-&nbsp;<a href='/saluto3_bis'>Saluto 3 BIS</a><br /><br />"
    html += "<strong>Funzioni:</strong> &nbsp;<br /><a href='/libri'>Lista Libri</a><br /><br />"

    return html

def lista_libri(id=0):
    lista = [
        ["1","Il vecchio e il mare", "Ernest Hemingway", "1952", "Un uomo può essere distrutto, ma non sconfitto."],
        ["2","Ventimila leghe sotto i mari", "Jules Verne", "1873", "L'anno 1866 fu caratterizzato da uno strano ..."],
        ["3","Fallout - Senza futuro", "Vault Tec", "2011", "Siamo fottuti! Così inizia l'autore nel libro..."]
    ]
    listaid =[]
    if (int(id) > 0 or str(id) != ""):
        for libroid in lista:
            if int(libroid[0]) == int(id):
                listaid.append(libroid)
                lista = listaid
                break

    html= "<table border=1>"
    html += "<tr><th>Titolo</th><th>Autore</th><th>Anno</th><th>Trama</th><th>Azioni</th></tr>"
    for libro in lista:
        html += "<tr>"
        
        if int(id) > 0:
            html += "<td>" + libro[1]  + "</td>"
        else:
            html += "<td><a href='/libri/" + str(libro[0]) + "'>" + libro[1]  + "</a></td>"

        html += "<td>" + libro[2]  + "</td>"
        html += "<td>" + libro[3]  + "</td>"
        html += "<td>" + libro[4]  + "</td>"

        # colonna elimina
        html += "<td>Elimina</td>"
        html += "<td><button onclick='eliminalibro(25)'>Elimina</button></td>"(" + libro[idendit] + ")

        html += "</tr>"
        html += "</table>"
    return html