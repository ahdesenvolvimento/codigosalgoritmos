def main():
    recursos = int(input('Digite a quantidade de recursos: '))
    existente, disponivel = [], []

    for i in range(recursos):
        qnt_cada_recursos = int(input('\tDigite a quantidade do recurso {}: '.format(i+1)))
        existente.append(qnt_cada_recursos)
        disponivel.append(qnt_cada_recursos)
    processos = int(input('\nDigite a quantidade de processos: '))
    print('Total de recursos existentes: ---> %s\n' % existente)
    matriz = criar_matriz(processos, recursos)
    preencher_matriz(matriz, disponivel)
    show(matriz)
    print()
    matriz_requisicao = criar_matriz(processos, recursos)
    preencher_matriz_requisicao(matriz_requisicao)
    show(matriz_requisicao)

    if checar(matriz_requisicao, disponivel):
        print('SEM DEADLOCK!!')
    else:
        print('TEM DEADLOCK!!')


def criar_matriz(processos, recursos):
    matriz = [0] * processos
    for i in range(len(matriz)):
        matriz[i] = [0] * recursos
    return matriz


def show(matriz):
    print('Mostrar a matriz preenchida!!')
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print()


def preencher_matriz(matriz, recurso):
    print('Preencha a matriz de alocação corrente!!')
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input('Digite o valor da linha {} e coluna {}: '.format(i, j)))
            variavel = recurso[j] - matriz[i][j]
            recurso[j] = variavel
            print('Recursos disponíveis atualizados!!')
            print('Recursos disponíveis: ',recurso,'\n')
    print('\nMatriz Preenchida!')


def preencher_matriz_requisicao(matriz):
    print('Preencher matriz de requisições!!')
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input('Digite o valor da linha {} e coluna {}: '.format(i, j)))

    print('Matriz Preenchida!')


def checar(matriz, recurso):
    for i in range(len(matriz)):
        variavel = True
        for j in range(len(matriz[i])):
            if matriz[i][j] > recurso[j]:
                variavel = False
    return variavel

main()