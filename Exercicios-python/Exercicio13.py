# Objetivo: Receber a quantidade de alimento em quilos. Calcular e mostrar quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
quantidadeQuilos = float(input("Digite aqui a quantidade de alimento (em quilos): "))
duracaoAlimento = float(quantidadeQuilos * 1000 / 50)

print("Este alimento durará: ", duracaoAlimento, "dias")