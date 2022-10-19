import random

jogarNovamente= "s";
jogadas = 0;
quemJOga = 2; #1 == CPU 2==Jogador
maxJogadas = 9;
vit = "n"
velha = [
      [" "," ", " "],
      [" ", " "," "],
      [" "," "," "],
]

def tela():
    global velha;
    global jogadas;

    print("   0  1  2 ");
    print("0: " + str(velha[0][0]) + " | " + str(velha[0][1]) + " | " + str(velha[0][2]));
    print("   ---------------");
    print("1: " + str(velha[1][0]) + " | " + str(velha[1][1]) + " | " + str(velha[1][2]));
    print("   ---------------");
    print("2: " + str(velha[2][0]) + " | " + str(velha[2][1]) + " | " + str(velha[2][2]));

    print("   ---------------");
    print("Jogadas :" + str(jogadas));

tela();

def jogadorJoga():
    global jogadas;
    global quemJoga;
    global vit;
    global maxJogadas;
    if (quemJoga==2 and jogadas<maxJogadas):
        l = int(input("Informe a linha: "));
        c = int(input("Informe a coluna: "));
        try:
            while (velha[l][c] != " "):
                    l = int(input("Informe a linha: "));
                    c = int(input("Informe a coluna: "));
            velha[l][c] = "X";
            quemJoga = 1;
            jogadas+=1;
        except:
            print("Linha ou Coluna Invalida");
            vit='n';
def cpuJoga():
    global jogadas;
    global quemJoga;
    global vit;
    global maxJogadas;
    if (quemJoga==1 and Jogadas<maxJogadas):
        l = random.randrange(0,3);
        c = random.randrange(0,3);
        while(velha[l][c] != " "):
            l = random.randrange(0, 3);
            c = random.randrange(0, 3);
        velha[l][c]=" O ";
        quemJoga = 2;
        jogadas +=1;

def verificarVitoria():
    global velha;
    global vit;
    vit = "n";
    simbolos=["X","O"];
    for s in simbolos:
        vit="n"
        #verificar vitorias em linhas
        il=ic=0;
        while(il<3):
            soma=0;
            ic = 0;
            while(ic<3):
                if(velha[il][ic] == s):
                    soma+=1;
                ic +=1;

            if(soma==3):
                vit= s
                break
            il += 1;
        if(vit!="n"):
            vitoria=s;
            break;
            #verificar coluna
            il = ic = 0;
            while (ic < 3):
                soma = 0;
                il = 0;
                while (il < 3):
                    if (velha[il][ic] == s):
                        soma += 1;
                    il += 1;
                if (soma == 3):
                    vit = s
                    break
            if (vit != "n"):
                vitoria = s;
                break;

    print()


while True:
    tela();
    jogadorJoga();
    cpuJoga();

