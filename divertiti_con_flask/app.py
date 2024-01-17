from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/saluto1")
def saluto1():
    return "Ciao abbelli! Questo è il saluto 1!"


@app.route("/saluto2")
def saluto2():
    return "Il saluto 2 e' qui e dice: AJOO!"

@app.route("/saluto3")
def saluto3():
    return "Saluto 3 e' meglio di me e di te!"

@app.route("/saluto<i>_bis")
def saluto_bis(i):
    saluto = ""
    print(i)
    if i== "1": saluto = "Ciao abbelli! Questo è il saluto 1_BIS!"
    if i== "2": saluto = "Il saluto 2_BIS e' qui e dice: AJOO!"
    if i== "3": saluto = "Saluto 3_BIS e' meglio di me e di te!"
    return saluto

@app.route("/testo/<t>")
def testo(t):
    testo =""
    if t == "m": testo = media()
    if t == "f": testo = fattoriale()
    if t == "p": testo = potenza()
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
    stringa = "Il numero " + str(numero) + " eevato a potenza e' " + str(potenza)
    return stringa
    
    