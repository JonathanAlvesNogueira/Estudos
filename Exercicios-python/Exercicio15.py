# Objetivo: Receber os valores de 2 catetos de um triângulo retângulo. Calcular e mostrar a hipotenusa.
cat1 = int(input("Informe o valor do primeiro cateto"));
cat2 = int(input("Informe o valor do segundo cateto"));
hip = ((cat1**2) + (cat2**2)) ** 0.5;
print(hip);