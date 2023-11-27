#Iperbole da matrice
import os , time

#pulisco schermo
os.system("cls" if os.name=="nt" else "clear" )


def bootstrap():
    time.sleep(0.1)
    print("------------------------------------------")
    time.sleep(0.1)
    print("#####   \33[96m IPEROLE DA MATRICE (x,y) \033[0m   ##### ")
    time.sleep(0.1)
    print("------------------------------------------")

#matrice
righe = 5
colonne = 25

bootstrap()
print()
print("Iperbole da matrice di valori x/y di 10 (x=10, y=10)")
print()
print()

#colonne di intestazione
print("  ", end="")
for n in range(colonne):
    c = n+1
    sColonna = "0" + str(c) if c < righe else c
    print(sColonna, end=" ")

print()

'''
x=r
y=c

y = x**2
'''

for r in range(righe):
    riga = r+1
    sRiga = "0" + str(r) if r < righe else r
    print(sRiga, end="")
    
    for c in range(colonne):
        mark = "-"
        colonna = c+1
        pos = c**2
        
        
        if r==pos:
            mark="*"
        else:
            mark=" "
        
        if c <= 0:
            print(" %s" %(mark), end="")
        else:
            print("  %s" %(mark) , end="")
        
        #print("  -", end="")
        
    print()
    
print()
print()
    