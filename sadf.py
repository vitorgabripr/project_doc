lista = []
lista = input("Digite 4 números: ")
lista.append(lista)
print (lista)

for i in len(lista):
    for j in lista[i]:
        temp = lista[i]
        lista[j] = lista[j + 1]
        lista[j + 1] = temp
print("Lista organizada: ",lista)
