import random
forca = """
____
   |
   |"""
   
inicio = """


"""
cabeca = """
   O
"""
tronco = """
   O
   |
"""
bracoe = """
   O
  /|
"""
bracod = """
   O
  /|\
"""
pernae = """
   O
  /|\
  /   
"""
pernad = """
   O
  /|\
  / \  
"""

lista = [
    inicio,
    cabeca,
    tronco,
    bracoe,
    bracod,
    pernae,
    pernad
]


palavras = vetor = ["SESI", "SENAI", "MARCELO", "IGOR"]
palavra_secreta =  random.choice(palavras)
letras_erradas = ""
letras_acertadas = " "
tentaivas =  6
acertos = 0 
erros = 0





print ("================================================================== \n")
print ("Jogo da forca \n")
print ("================================================================== \n")



while tentaivas != 0 :
    mensagem = ""
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            mensagem += letra
        else:
            mensagem += "_ "
            
            
    print (f"{mensagem}")
    print (f"{forca + lista [erros]}")
    print (f"{letras_erradas }")
    print (f"Restam: {tentaivas} tentativas\n")
    
    letra = input("Digite uma letra: \n")

    
    if letra in palavra_secreta:
        print("Você acertou uma letra, parabéns!\n")
        print("=============================================================")
        acertos += acertos + 1 
        letras_acertadas += letra 
    else:
        print("A palavra não possui essa letra, :( \n")
        print("=============================================================")
        erros += 1
        letras_erradas += letra
        tentaivas += - 1
        
    mensagem = ""
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            mensagem += letra
        else:
            mensagem += "_ "
        
        
    if mensagem == palavra_secreta:
        print("Você ganhou!")
       
    

if tentaivas <= 0:
    print("Você perdeu!")

        
        
        
    
  
    