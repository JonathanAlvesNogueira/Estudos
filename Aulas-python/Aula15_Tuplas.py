carros = ["HRV", "Golf", "Gol", "Camaro"];
carros1 = ("Hrv", "Gol", "Celta");
carros2 = list(carros1);
carros2[1] = "Camaro";
carros1 = tuple(carros2);


for x in carros1:
    print(x);