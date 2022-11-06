# Objetivo: Receber 2 ângulos de um triângulo. Calcular e mostrar o valor do 3º ângulo.
ang1 = int(input("Informe o valor do angulo 1"));
ang2 = int(input("Informe o valor do angulo 2"))
ang3 = (180 - (ang1+ang2));
print(ang3);