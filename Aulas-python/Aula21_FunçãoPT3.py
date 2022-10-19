valores=[1,2,3,4];
def somar(num):
    r = 0;
    for n in num:
        r+=n;
    return r;
def valLista(num):
    for v in num:
        print(v);

valLista(valores);
print("Esse é o resultado solicitado: "+ str(valores) +" : " + str(somar(valores)));