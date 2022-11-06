import json;

carros_json='{"marca": "Honda", "modelo":"HRV", "cor":"preto"}'
carros = json.loads(carros_json);

for i,v in carros.items():
    print(i + "  " + v);