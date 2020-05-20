from utils_matrizes import *

NOME_ARQUIVO = 'cadastro_de_bovinos.txt'

def main():
    ingredientes = abrir_arquivo(NOME_ARQUIVO)
    menu = '\n1 - Listar ingredientes\n' \
           '2 - Adicionar novo ingrediente\n' \
           '3 - Remover ingrediente\n' \
           '4 - Buscar por caracteristica\n' \
           '5 - Editar o preço do ingrediente' \
           '0 - Exit!\n' \
           'Opção: '
    opcao = int(input(menu))
    while opcao != 0:
        if opcao == 1:
            print('\nListar os ingredientes!')
            listar(ingredientes)

        elif opcao == 2:
            print('\nAdicionar um novo ingrediente!')
            ingredientes = adicionar(ingredientes)

        elif opcao == 3:
            print('Remoção de ingredientes!')
            ingredientes = remover_ingrediente(ingredientes)

        elif opcao == 4:
            opcao_2 = int(input(menu_opcao_quatro()))
            if opcao_2 == 1:
                buscar_tipo(ingredientes)
            elif opcao_2 == 2:
                buscar_nome(ingredientes)
            elif opcao_2 == 3:
                buscar_preco(ingredientes)
            elif opcao_2 == 4:
                buscar_peso(ingredientes)

        elif opcao == 5:
            ingredientes = editar_preco(ingredientes)

        else:
            print('\nOpção Inválida!')
        opcao = int(input(menu))
    salvar_arquivo(NOME_ARQUIVO, ingredientes)


#    input('Limpar o menu!')
#   os.system('cls')

def novo_ingrediente():
    ingredientes = new_vetor(4)
    ingredientes[0] = input('\tTipo do ingrediente: ')
    ingredientes[1] = input('\tNome do ingrediente: ')
    ingredientes[2] = input('\tDigite o preço do ingrediente: ')
    ingredientes[3] = input('\tDigite o peso do ingrediente (em KG): ')

    return ingredientes

def remover_ingrediente(ingrediente):
    nova_matriz = cria_matriz(len(ingrediente)-1, len(ingrediente[0]))
    tipo = input('Digite o tipo do alimento que deseja retirar! ')
    nome = input('Digite o nome do alimento que deseja retirar! ')
    preco = input('Digite o preço do alimento que deseja retirar! ')
    peso = input('Digite o peso do alimento que deseja retirar! ')
    for i in range(len(ingrediente)):
        #print(i)
        if tipo != ingrediente[i][0]:
            nova_matriz = inserir_elemento(nova_matriz, ingrediente[i][0])
            #print(nova_matriz[i)
        if nome != ingrediente[i][1]:
            nova_matriz = inserir_elemento(nova_matriz, ingrediente[i][1])
            #print(nova_matriz)
        if preco != ingrediente[i][2]:
            nova_matriz = inserir_elemento(nova_matriz, ingrediente[i][2])
            #print(nova_matriz)
        if peso != ingrediente[i][3]:
            nova_matriz = inserir_elemento(nova_matriz, ingrediente[i][3])
            #print(nova_matriz)
    print(nova_matriz)
    return nova_matriz


def editar_preco(ingredientes):
    nome = input('Digite o nome do ingrediete: ')
    preco = input('Digite o novo preço: ')
    for i in range(len(ingredientes)):
        if nome == ingredientes[i][1]:
            ingredientes[i][2] = preco
    return ingredientes


def adicionar(ingrediente):
    return inserir_elemento(ingrediente, novo_ingrediente())


def buscar_nome(ingredientes):
    nome = input('Digite o nome do(s) ingrediente: ')
    for i in range(len(ingredientes)):
        if nome == ingredientes[i][1]:
            print(ingredientes[i])


def buscar_tipo(ingredientes):
    tipo = input('Digite o tipo do(s) ingrediente: ')
    for i in range(len(ingredientes)):
        if tipo == ingredientes[i][0]:
            print(ingredientes[i])


def buscar_preco(ingredientes):
    preco = input('Digite o preço do(s) ingrediente: ')
    for i in range(len(ingredientes)):
        if preco == ingredientes[i][2]:
            print(ingredientes[i])


def buscar_peso(ingredientes):
    peso = input('Digite o peso do(s) ingrediente: ')
    for i in range(len(ingredientes)):
        if peso == ingredientes[i][3]:
            print(ingredientes[i])

def listar(ingredientes):
    print('TIPO|NOME|PREÇO|PESO')
    show_matriz(ingredientes)

def menu_opcao_quatro():
    menu = '1 - Buscar por tipo\n' \
           '2 - Buscar por nome\n' \
           '3 - Buscar por preço\n' \
           '4 - Buscar por peso\n' \
           'Opção: '
    return menu

def abrir_arquivo(nome_do_arquivo):
    ingredientes_prontos = cria_matriz(0, 4)
    fin = open(nome_do_arquivo)
    linhas = fin.readlines()
    fin.close()
    for i in range(len(linhas)):
        ingrediente = linhas[i].strip().split('*')
        ingredientes_prontos = inserir_elemento(ingredientes_prontos, ingrediente)
    return ingredientes_prontos


def salvar_arquivo(nome_arquivo, ingredientes_prontos):
    fout = open(nome_arquivo, 'w')
    for i in range(len(ingredientes_prontos)):
        linha = '%s*%s*%s*%s\n' % (ingredientes_prontos[i][0], ingredientes_prontos[i][1], ingredientes_prontos[i][2], ingredientes_prontos[i][3])
        fout.write(linha)
    fout.close()


if __name__ == '__main__':
    main()
