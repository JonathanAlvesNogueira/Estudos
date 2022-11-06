# Objetivo: Receber o valor de um depósito em poupança. Calcular e mostrar o valor após 1 mês de aplicação sabendo que rende 1,3% ao mês.
deposito = float(input("Informe o valor do deposito"));
aplicado = deposito + (deposito* 0.013);
print("Esse é o valor aplicado depois de um mês" + str(aplicado));
