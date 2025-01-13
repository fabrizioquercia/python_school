class Alunno:

    fileCsv = "data/alunni.csv"
    #self, nome, cognone, classe, matricola, contatti
    
    def __init__(self):
        '''self.nome = nome
        self.cognome = cognone
        self.classe = classe
        self.matricola = matricola
        self.contatti = contatti'''
        pass
    
    def getListaCompleta(self, excludeFirst=True):
        f = open("data/alunni.csv")
        inx = 1 if excludeFirst else 0
        lines = f.readlines()[inx:]
        for dati in lines:
            dato = dati.split(";")
            dato = dati.split()
            print("Dato: ", dato)


alunni = Alunno()
alunni.getListaCompleta()




class Esame:
    def __init__(self) -> None:
        pass


class Corso:
    def __init__(self) -> None:
        pass