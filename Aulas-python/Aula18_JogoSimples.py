import random;
import os;

erros = 0;
sorteado =  random.randrange(0,100);
jogador = int(input("Digite seu numero: "));
while(sorteado != jogador):
    os.system('cls');
    if(sorteado>jogador):
        print("[ERRO] Numero sorteado é maior");
    elif(sorteado < jogador):
        print("[ERRO] Numero sorteado é menor que jogador");
    erros+=1;
    jogador = int(input("Digite seu numero: "));
print("Numero: " + str(jogador) + ", Você acertou em: " + str(erros+1) + "Tentativas");


