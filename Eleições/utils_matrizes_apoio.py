def new_vetor(tamanho):
    return [0] * tamanho


def preencher_vetor(vetor):
    for i in range(len(vetor)):
        elemento = input('Digite o elemento da posição {} do vetor em questão!'.format(i))
        vetor[i] = elemento
    return vetor


def preencher_vetor_inteiro(vetor):
    for i in range(len(vetor)):
        elemento = input('Digite o elemento da posição {} do vetor em questão!'.format(i))
        vetor[i] = int(elemento)
    return vetor


def bubble_sort(vetor):
    variavel = 0
    ordenou = True
    for i in range(1, len(vetor)):
        if vetor[i - 1] > vetor[i]:
            variavel = vetor[i - 1]
            vetor[i - 1] = vetor[i]
            vetor[i] = variavel
            ordenou = False
    if ordenou:
        return
    else:
        bubble_sort(vetor)


def bubblesort(lista):
    for x in range(len(lista)-1,0,-1):
        for i in range(x):
            if lista[i]>lista[i+1]:
                j = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = j


def inverter_vetor(vetor1, vetor2):
    for i in range(len(vetor1)):
        vetor2[i] = vetor1[len(vetor1) - 1 - i]
    return vetor2


def vetorc(vetora, vetorb, vetorc, tamanho_vetor):
    vetorc = new_vetor(tamanho_vetor * 2)
    for i in range(len(vetora)):
        vetorc[i] = vetora[i]
    for j in range(len(vetorb)):
        vetorc[j + tamanho_vetor] = vetorb[j]
    return vetorc


def inserir_elemento(vetor, item):
    novo_vetor = new_vetor(len(vetor) + 1)
    for i in range(len(vetor)):
        novo_vetor[i] = vetor[i]
    novo_vetor[len(novo_vetor) - 1] = item
    return novo_vetor


def remover(matriz, posicao):
    nova_matriz = cria_matriz(len(matriz)-1)
    j = 0
    for i in range(len(matriz)):
        if i != posicao:
            nova_matriz[j] = matriz[i]
            j += 1

    return nova_matriz


def cria_matriz(linhas, colunas):
    matriz = [0] * linhas
    for i in range(len(matriz)):
        matriz[i] = [0] * colunas
    return matriz


def show_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')

        print()


def preencher_matriz_linhas(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz) - 1):
            matriz[linha][coluna] = int(input('Digite o elemento: '))


def preencher_matriz_coluna(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz) + 1):
            matriz[linha][coluna] = int(input('Digite o elemento: '))


def matriz_quadrada(ordem):
    nova_matriz = [0] * ordem
    for i in range(len(nova_matriz)):
        nova_matriz[i] = [0] * ordem
    return nova_matriz


def preencher(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = int(input())

