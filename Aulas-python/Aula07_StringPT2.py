curso = "Curso de python";
nome = "Jonathan";
res = "python" in curso;
print(res);

#negação
res2 = "python" not in curso;
print(res2)
""""
res = curso + nome;
print(res);
"""
cidade = "belo horizonte";
dia = 15;
mes = "dezembro"
ano = 2022;
data="{}, {} de {} de {}"

print(cidade + ", " + str(dia) + " de " + mes + " de " + str(ano));
print(data.format(cidade, dia, mes, ano))