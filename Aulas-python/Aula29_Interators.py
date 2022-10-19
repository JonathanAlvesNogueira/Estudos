carros =["HRV", "Honda", "Camaro", "Ferrari"];
itCarros=iter(carros);
print(next(itCarros));

itCarro= iter(carros);
while itCarro:
    try:
        print(next(itCarro));
    except StopIteration:
        print("Fim");
        break;

