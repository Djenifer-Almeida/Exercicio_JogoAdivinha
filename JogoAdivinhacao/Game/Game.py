import random # <-- Inclusão do módulo 'random'//
numSecret = random.randint(1,100) # <--- Gerador de número aleatório(1 a 100)//
tentativas = 0
#--- Mensagem ---#
print("")
print("------------------ JOGO DE ADIVINHAÇÃO ------------------")
print("")
print("Digite um número de 1 a 100, e vamos ver se você adivinha.")
#-- Condições --#
while True:
        print("")
        adivinha = int(input("Digite seu palpite: "))
        tentativas += 1 # <-- Contador das tentativas//

        if adivinha == numSecret:
            print(f"Oba! Você conseguiu em {tentativas} tentativas.")
            break # <-- Fechamento do bloco//

        elif adivinha < numSecret:
            print("Tente um número maior.")
            print("")
        else:
            print("Tente um número menor.")
            print("")

            
  