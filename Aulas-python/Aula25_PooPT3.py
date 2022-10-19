class NPC:
    def __init__(self, nome, time, forca,municao):
        self.nome = nome;
        self.time = time;
        self.forca = forca;
        self.municao = municao;
        self.vivo =  True;
        self.energia = 100;

    def info(self):
        print("nome = " + self.nome);
        print("time: " + str(self.time));
        print("forca: "+ str(self.forca));
        print("munição: " + str(self.municao));
        print("vivo: " + str(self.vivo));
        print("Energia: " + str(self.energia));
        print("_________________________________")

class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200;
        self.municao = 200;
        super().__init__(nome, time, self.forca,self.municao)

class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100;
        self.municao = 20;
        super().__init__(nome, time, self.forca, self.municao)
        def inf(self):
            super().info();


si = Guarda(nome="Ola", time=1);
s2 = Soldado(nome="Anderson", time=2)
si.info()
s2.info()
