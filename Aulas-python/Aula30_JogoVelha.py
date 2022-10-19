
jogarNovamente= "s";
jogadas = 0;
quemJOga = 2;
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