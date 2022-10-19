carros = ["HRV","FORD","FUSION","GOLF"];
i = 0;
tam = len(carros);
while i< 9:
    print(i);
    i+= 1;
    if(i>=tam):
        print(carros[i-1]);
        break;
print("Fim do Loop");