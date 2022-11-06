# Objetivo: Receber os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcular e mostrar as raízes reais (considerar que a equação possui 2 raízes)
a = int(input("Informe o valor de A"));
b = int(input("Informe o valor de B"));
c = int(input("Informe o valor de C"));
delta = b**2 - (4*a*c);
if(delta>0):
    x1 = -(b) + (delta**(1/2));
    x2 = - (b) - (delta**(1/2));
    print(x1);
    print(x2);
else:
    print("Essa equação não possui 2 raizes reais");

