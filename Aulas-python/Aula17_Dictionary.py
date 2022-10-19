#Chave/key - Valor/value
"""

carro = {"Fabricante" : "Honda",
         "Modelo" : "HRV",
         "Ano" : "2016",
         "Cor":"Prata"
}
carro["Estado"] = "Limpo";

carro.pop("Modelo");
del carro["Estado"];


fab = carro.get("Modelo");
carro["Cor"] = "Preto";

#print(carro["Modelo"]);
print(carro["Ano"]);
print(fab)
print(carro["Cor"])


for x in carro:
    print(x)# chave
    print(carro[x]); # valor

if "Modelo" in carro:
    print("Sim, tem modelo dentro de carro");

for c,v in carro.items():
    print(c + ":" + v)

print("Esse é o tamanho do nosso dictionary " + str(len(carro)));
"""



carros={
    "Carro1":{
        "Fabricante":"Ford",
        "Modelo" : "Honda"
},
    "Carros2":{
        "Fabricante": "Ferrari",
        "Modelo" : "Ferrari"
},
    "Carros3":{
        "Fabricante": "Renault",
        "Modelo":"Fusion"
    }
}
print(carros["Carro1"]["Fabricante"]);





