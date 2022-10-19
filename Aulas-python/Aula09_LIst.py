carros = ["HRV", "Golf", "Argos", "Gol"];
carros[3] = "Fusion";
carros.append("Fit");
carros.append("Fusca")
print(str(len(carros)));
carros.remove("Fusion");
carros.pop()

del carros[2]
carros2 = list(carros);
carros


print(carros);