# def soma_lista(lista):
#     soma = 0
#     for elemento in lista:
#         soma += elemento
#     return soma

# lista = [1, 2, 3, 4, 5]
# print(soma_lista(lista))

#Ordena por ordem alfabética, insira os elementos através do imput
def ordena_lista(lista):
    return sorted(lista)

def main():
    lista = []
    while True:
        elemento = input("Insira um elemento para a lista (ou 'fim' para terminar): ")
        if elemento.lower() == 'fim':
            break
        lista.append(elemento)
    print("Lista ordenada:", ordena_lista(lista))

if __name__ == "__main__":
    main()