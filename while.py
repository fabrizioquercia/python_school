import os
import random
import time


os.system("cls" if os.name=="nt" else "clear")
time.sleep(0.7)

random1 = random.randrange(10, 40)
random2 = random.randrange(20, 60)
diff = (random2-random1)
numero = 1

print("Random1:", random1, "- Random2:", random2)
print("Random2 - Random1=", (random2-random1), "(diff)")
print("Numero:",sep=" ", end=" ", flush=True)

while ( numero <= random1 or numero > (random2-random1) ):
    
    if random1 > random2:
        print("\n[random1 > random2]\nEsco perchè random1 è maggiore di random2")
        break
    
    if random1 == 20:
        print("\n[random1 == 20]\nEsco perchè random1 è = 20")
        break
        
    if numero > diff:
        print("\n[numero > diff]\nEsco perchè il numero", numero, "ha superato la differenza fra (random2-random1 =", diff ,")")
        break
        
    if numero > random1:
        print("\n[numero > random1]\nEsco perchè il numero è maggiore di random1")
        break
    
    time.sleep(0.07)
    print(numero, sep=" ", end=" ", flush=True)
    numero = numero+1
