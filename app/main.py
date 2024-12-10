import json
import os
import argparse

class Menu:
    # Função para ler um arquivo JSON
    @staticmethod
    def ler_json(caminho_arquivo):
        if not os.path.exists(caminho_arquivo):
            print(f"Arquivo {caminho_arquivo} não encontrado.")
            return None
        with open(caminho_arquivo, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                print(f"Erro ao decodificar JSON: {e}")
                return None
        return data

    # Função para salvar dados em um arquivo JSON
    @staticmethod
    def salvar_json(caminho_arquivo, dados):
        with open(caminho_arquivo, 'w') as file:
            json.dump(dados, file, indent=4)
        print(f"Dados salvos em {caminho_arquivo} com sucesso.")

    # Função para adicionar ou atualizar dados
    @staticmethod
    def adicionar_dados(data, novos_dados):
        data.update(novos_dados)
        return data

    # Função para adicionar uma nova URL e título à documentação
    @staticmethod
    def adicionar_documentacao(caminho_arquivo, titulo, url):
        data = Menu.ler_json(caminho_arquivo) or {}
        if "documentacao" not in data:
            data["documentacao"] = []
        data["documentacao"].append({"titulo": titulo, "url": url})
        Menu.salvar_json(caminho_arquivo, data)

def exibir_menu():
    print("Menu:")
    print("1. Ler o arquivo JSON")
    print("2. Salvar dados no arquivo JSON")
    print("3. Adicionar URL e título à documentação")
    print("4. Sair")

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            caminho_arquivo = input("Informe o caminho para o arquivo JSON: ")
            dados = Menu.ler_json(caminho_arquivo)
            if dados:
                print(dados)

        elif escolha == '2':
            caminho_arquivo = input("Informe o caminho para o arquivo JSON: ")
            dados_str = input("Informe os dados a serem salvos (no formato JSON): ")

            try:
                novos_dados = json.loads(dados_str)
            except json.JSONDecodeError:
                print("Erro: Os dados fornecidos não estão em formato JSON válido.")
                continue

            dados = Menu.ler_json(caminho_arquivo) or {}
            dados_atualizados = Menu.adicionar_dados(dados, novos_dados)
            Menu.salvar_json(caminho_arquivo, dados_atualizados)

        elif escolha == '3':
            caminho_arquivo = input("Informe o caminho para o arquivo JSON: ")
            titulo = input("Informe o título da documentação: ")
            url = input("Informe a URL da documentação: ")
            Menu.adicionar_documentacao(caminho_arquivo, titulo, url)

        elif escolha == '4':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
