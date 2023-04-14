import json

with open('usuarios1.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Converter arquivo JSON -> String
    print(data["nome"])

with open('usuarios2.json', encoding='utf-8') as arquivo2_json:
    data = json.load(arquivo2_json)
    print(data["permissão"][1])