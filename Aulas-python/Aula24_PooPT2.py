class Carro:
    velMax = 0;
    ligado = False;
    cor = "";

    def __init__(self, v, l, c):
        self.velMax = v;
        self.ligado = l;
        self.cor = c;

    def mostrar(self):
        print("Essa é a velocidade maxima: " + str(self.velMax));
        print("Essa é a condição, se está ligado ou não:  " + str(self.ligado))
        print("Essa é a cor do carro:  " + self.cor);
    def Ligar(self):
        self.ligado = True;
    def Desligar(self):
        self.ligado = False;
    def Andar(self):
        if(self.ligado):
            print("Está andando");
        else:
            print("Carro desligado")

c1 = Carro(200, True, "Vermelho");
c2 = Carro(20, False, "Azul")
c3 = Carro(10, True, "Verde")

c2.Ligar();
c2.mostrar()
