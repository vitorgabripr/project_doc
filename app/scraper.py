import json
import os
import argparse


# Abrir e ler um arquivo JSON
with open('arquivo.json', 'r') as file:
    data = json.load(file)  # Converte JSON em um dicionário Python

print(data)
data = {
    "nome": "Vitor",
    "idade": 18,
    "habilidades": ["Python", "Finanças", "Empreendedorismo"]
}

# Criar/Salvar dados em um arquivo JSON
with open('arquivo.json', 'w') as file:
    json.dump(data, file, indent=4)  # `indent` adiciona espaçamento para legibilidade
data['cidade'] = 'Gravataí'
json_string = '{"nome": "Vitor", "idade": 18}'
data = json.loads(json_string)  # Converte string JSON para dicionário

print(data['nome'])  # Acessa o valor da chave "nome"
data = {"nome": "Vitor", "idade": 18}
json_string = json.dumps(data, indent=4)

print(json_string)  # Saída como uma string formatada
data['idade'] = 19
del data['habilidades']
{"nome": "Vitor", "idade": 18}
{"nome": "Gabriel", "idade": 25}
with open('arquivo.jsonl', 'r') as file:
    for line in file:
        record = json.loads(line)
        print(record)
