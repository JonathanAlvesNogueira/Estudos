# Objetivo: Receber os valores de x e y. Efetuar a troca de seus valores e mostrar seus conteúdos.
x = int(input("Informe o valor de x"))
y = int(input("Informe o valor de Y"));
aux = x;
x = y;
y = aux;
print(str(x) + " valor trocado " + str(y));