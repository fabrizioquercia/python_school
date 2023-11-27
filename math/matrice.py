import os 

def cls():
    os.system("cls" if os.name=="nt" else "clear" )


#matrice
righe_default = 10
colonne_default = 10


righe = int( input("Quante righe vuoi? ") )
colonne = int( input("Quante colonne vuoi? ") )

if righe <= 0 or righe=="": righe = righe_default
if colonne <= 0 or colonne=="": colonne = colonne_default

#cls()
print()

for c in range(colonne):
    if c==0:
        print("   " + str(c+1), end=" ")
    else:
        if c+1 > 9:
            
            v = str(c+1)
            v = v[1:2]
            
            #print("m=%s v=%s c=%s" %(1, v, c) )
            
            print(v, end=" ")
        else:
            print(c+1, end=" ")

print()
print("   ", end="")
for rg in range(colonne*2): print("-", end="")
print()
        
for r in range(righe):
    if r<10:
        print("  " + str(r+1), end="! ")
    else:
        print("" + str(r+1), end="! ")
    print()

#cls()


for n in range(5, 0, -1):
    print("%s (%s)" %(n, n-1) )