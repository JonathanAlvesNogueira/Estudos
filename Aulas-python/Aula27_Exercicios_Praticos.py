carro = []

class Carro:
    nome=""
    ligado = False;
    pot=0;
    velMax = 0;
    def __init__(self, nome, velMax, pot, ligado):
        self.nome = nome
        self.pot = pot;
        self.velMax = int(pot)*2;
        self.ligado=False;
    def Ligar(self):
        self.ligado = True;
    def Desligar(self):
        self.ligado = False;
    def info(self):
        print("Nome: " + self.nome);
        print("Potencia:" + str(self.pot));
        print("Velocidade Máxima" + str(self.velMax));
        print("Ligado: " + str("Sim" if self.ligado else "Não"))
def menu():
    print("1-Novo carro")
    print("2-Informações do carro");
    print("3- Excluir o carro");
    print("4- Ligar o carro");
    print("5-Desligar o carro");
    print("6- Listar carro");
    print("7- sair do menu");
    return opc;
def NovoCarro():
    n = input("Nome do carro: " +);
    p = input("Potencia do carro: ");
    car = carro(n,p);
    carro.append(car);
    print("novo carro criado");

def informacoes():
    n = input("Informe o numero do carro que deseja ver nas informaçoes");
    try:
        carro[int(n)].info;
    except:
        print("Carro não existe na lista");
def ExcluirCarro():
    n = input("Informe o numero do carro que deseja excluir: ");
    try:
        del carro[int(n)];
    except:
        print("Carro não existe na lista")
def CarroLIgar():
    n = input("Informe o numero do carro que deseja ligar: ");
    try:
        del carro[int(n)];
    except:
        print("Carro não existe na lista");
def CarroDesligar():
    n = input("Informe o numero do carro que deseja desligar: ");
    try:
        del carro[int(n)];
    except:
        print("Carro não existe na lista");
def ListarCarros():
    p = 0;
    for c in carro:
        print(str(p) + " - " + c.nome)
        p = p+1;