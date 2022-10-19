"""
def somar(n1, n2):
    r = n1 + n2;
    print(str(r));
somar(5,8);
somar(9,8)
"""


def textos(*t):
    for i in t:
        print(str(t));

    def somar(*num):
        r = 0;
        for n in num:
            r+=n;
        print(str(r));


    somar(5,2,3);
    textos("Canal", "Python");
def carro(ca):
    print("Modelo " + ca);

carro("Fiat");


