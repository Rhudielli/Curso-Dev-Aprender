# Criar ou ler um arquivo json

import json

computador_json = """{
    "marca": "Dell",
    "preco": 15000
}"""

# Lendo uma string JSON
data = json.loads(computador_json)
# print(data["preco"])

# Salvar uma string JSON -> Arquivo JSON

with open('computador.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(computador_json, arquivo_json)

# Para ler uma arquivo JSON
with open('computador.json', encoding='utf-8') as arquivo_json:
    string_computador_json = json.load(arquivo_json) # convertendo JSON -> String
    dicionario_computador_json = json.loads(string_computador_json) # Converter de string -> Dicionario python
    print(dicionario_computador_json["marca"])

###############################################################################################################################################################

# DESAFIO 🥇

usuario_json = """{
    "name": "John Smith",
    "age": 30,
    "city": "New York",
    "isStudent": true,
    "gpa": 3.5
}"""

with open('desafio.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(usuario_json, arquivo_json)