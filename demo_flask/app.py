from flask import Flask, request


FLASK = Flask(__name__)


@FLASK.route("/")
def hello_world():
    return "<h1>Piccola app in Flask!</h1>"

@FLASK.route("/saluto")
def saluto():
    return "Ciao abbelli! Questo è il saluto!"


@FLASK.route("/numero_as_int/<n>", methods = ['GET'])
def numero_as_int(n):
    print( type(n) )
    num = int(n)
    print( type(num) )
    return str(num * 2 / 3)

@FLASK.route("/salutami?nome=<nome>&cognome=<cognome>", methods = ['GET'])
def salutami():
    n = request.args.get('nome')
    return "Ciao " + "" + "!"
























'''
@FLASK.route("/saluto<i>_bis")
def saluto_bis(i):
    saluto = ""
    if i== "1": saluto = "Ciao abbelli! Questo è il saluto 1_BIS!"
    if i== "2": saluto = "Il saluto 2_BIS e' qui e dice: AJOO!"
    if i== "3": saluto = "Saluto 3_BIS e' meglio di me e di te!"
    return saluto

@FLASK.route("/testo/<t>")
def testo(t):
    testo =""
    if t == "m": testo = FN.media()
    if t == "f": testo = FN.fattoriale()
    if t == "p": testo = FN.potenza()
    return testo



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





def lista_libri():
    lista = [
        ["Libro1", "Autore 1", "2003", "Trama"],
        ["Libro 2", "Autore 2", "2025", "Qui la trama..."],
        ["Libro 3", "Autore 3", "1977", "E' vecchio sto libro, è del 77...."]
    ]
    html= "<table border=1>"
    html += "<tr><th>Titolo</th><th>Autore</th><th>Anno</th><th>Trama</th></tr>"
    for libro in lista:
        html += "<tr>"
        html += "<td>" + libro[0]  + "</td>"
        html += "<td>" + libro[1]  + "</td>"
        html += "<td>" + libro[2]  + "</td>"
        html += "<td>" + libro[3]  + "</td>"
        html += "</tr>"
    html += "</table>"
    return html