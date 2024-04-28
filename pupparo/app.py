import sqlite3 
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/")
def lista_libri() :
     
    x="libreria"
    y=sqlite3.connect(x)

    cursore=y.cursor()
    cursore.execute("SELECT * from libri")
    libro=cursore.fetchall()
    
    return libro

#main principale

def main () :
        
    #a=input("di quale anno è il libro che cerchi ? : ")
    #if a!="":
     #   anno(a)
        
    b=input("chi ha scritto il libro che cerchi ? : ")
    if b!="":
        autore(b)
        
    c=input("come si chiama il libro che stai cercando ? :")
    if c!="":
        titolo(c)
    else:
        x="libreria"
        y=sqlite3.connect(x)

        cursore=y.cursor()
        cursore.execute("SELECT * from libri")
        libro=cursore.fetchall()

        print(libro)
        

@app.route("/anno/<anno>")
def anno(anno):
    print(anno)
    x="libreria"
    y=sqlite3.connect(x)
    cursore=y.cursor()    
    cursore.execute("SELECT * from libri where anno = '"+anno+"'")
    libro=cursore.fetchall()
    return libro


@app.route("/autore/<autore>")
def autore(autore):
    x="libreria"
    y=sqlite3.connect(x)
    cursore=y.cursor()    
    #sautore = autore.replace(" ", "%")
    #sautore = sautore.replace("*", "%")
    
    sautore = autore.replace(" ", "%").replace("*", "%")
    
    
    cursore.execute("SELECT * from libri where autore like '%"+sautore+"%'")
    libro=cursore.fetchall()
    return libro

@app.route("/titolo")
def titolo(c):
    x="libreria"
    y=sqlite3.connect(x)
    cursore=y.cursor()
    cursore.execute("SELECT * from libri where titolo = '"+c+"'")
    libro=cursore.fetchall()
    print(libro)
main()

