# menu principal 
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    opcoes = {

        "1": lambda: print("Digite uma palavra chave: \n"),
        "2": lambda: print("Digite o título da documentação: \n"),
        "3": lambda: print("Mostrando todas documentações"),
        "4": lambda: exit("Saindo do programa...")
    }
    while True:
        print("\nMenu Principal\n")
        print("1. Buscar documentação\n")
        print("2. Adicionar documentação\n")
        print("3. Ver todas documentações\n")
        print("4. Sair\n")


        escolha = input()
        opcoes.get(escolha, lambda: print("Opção inválida."))()
        limpar_terminal()

menu()
