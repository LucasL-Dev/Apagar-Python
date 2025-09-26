import os
import random
import time

continuar = True;

while (continuar == True): 
    file_path = r"C:\Programação\Python\Apagar-Python\teste.txt"

    numero = random.randint(1,3)
    print (numero)
    numeroS = int(input("Digite um número:"))

    

    if (numeroS == numero):
        print ("Parabéns, nada foi apagado!")
        resposta = str(input("Quer tentar novamente?"))
        if (resposta != "Sim"):
            continuar = False
            break
    else:
        print ("Ih negão, já era, vamos apagar uma pasta ai")
        time.sleep(1)
        print ("5...")
        time.sleep(1)
        print ("4...")
        time.sleep(1)
        print ("3...")
        time.sleep(1)
        print ("2...")
        time.sleep(1)
        print ("1...")
        time.sleep(1)
        print ("Apagou....")
        os.remove (file_path)
        break
    
    
    