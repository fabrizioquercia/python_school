#Lezione oggi FRAZIONE
import os
os.system("cls" if os.name=="nt" else "clear" )


# ho una classe di N alunni, quindi devo cheidere il valore di N
numero_alunni = int(input("Inserisci il numero di alunni: "))

#voti = []
# inizializzo un vettore per ogni elemento di N e lo inizializzo a 0
voti = [ 0 for i in range(numero_alunni) ]
#print(voti)


# faccio inserir ei voti di ogni alunno in trentesimi e salvo in un vettore
for i in range(numero_alunni):
    voto = 100
    while voto > 30 or voto < 0:
        voto = int( input("Inserisci il voto in 30esimi dell'alunno %d: "%(i+1) ) )
        voti[i] = voto
print(voti)

# ciclo for con x,y
for x,y in enumerate(voti, start=0):
    #print(">> x=%d - y=%f" %(x, voti[y]) )
    pass
    

# scorro il vettore e riporto i voti in decimi
voti_in_decimi =[]
for voto in voti:
    # trasformo il voto in decimi
    voti_in_decimi.append(voto / 30 * 10)

# poi stampo
print(voti_in_decimi)

# potentissima programazione funzionale
l = [ round(voto/30*10) for voto in voti ]
print(l)


# alunni dizionario
alunno = {"nome":"Silvio", "cognome": "Di Gregorio"}
print(alunno)











# fine
print()
print("Programma terminato!")
print()
