import os
from utils_matrizes import *

nome_arquivo = 'cadastro_candidatos.txt'

def main():
    candidatos = abrir_arquivo(nome_arquivo)
    opcao = menu_principal()
    while opcao!= 0:
        if opcao == 1:
            print('\nListar todos os candidadatos a vereador cadastrados!')
            listar_candidatos(candidatos)
        elif opcao == 2:
            candidatos = adicionar_candidato(candidatos)
            salvar_arquivo(nome_arquivo, candidatos)
        elif opcao == 3:
            opcao2 = menuzinho()
            if opcao2 == 1:
                modificar_nome(candidatos)
            elif opcao2 == 2:
                modificar_partido(candidatos)
        elif opcao == 4:
            buscar_por_partido(candidatos)
        opcao = menu_principal()
        #input('\nLimpar....')
        #os.system('cls')


def cadastrar_novo_candidato():
    candidato = new_vetor(6)
    print('***--->>>\tInicializar o cadastro de um novo candidato!\t<<<---***\n')
    candidato[0] = input('\t\t\tDigite o nome do candidato: ')
    candidato[1] = input('\t\t\tDigite a idade do candidato {}: '.format(candidato[0]))
    candidato[2] = input('\t\t\tDigite a profissão do candidato {}: '.format(candidato[0]))
    candidato[3] = input('\t\t\tDigite o partido do candidato {}: '.format(candidato[0]))
    candidato[4] = input('\t\t\tDigite o número do candidato {}: '.format(candidato[0]))
    candidato[5] = input('\t\t\tDigite o nome como o candidato será chamado: ')
    print('\nCadastro do candidato {} foi efetuado com sucesso!!'.format(candidato[0]))
    return candidato


def adicionar_candidato(candidatos):
    return inserir_elemento(candidatos, cadastrar_novo_candidato())


def listar_candidatos(candidatos):
    print('\t\t\tNome | Idade | Profissão | Partido | Numero | Apelido')
    for i in range(len(candidatos)):
        print('Candidato {}: '.format(i+1), candidatos[i])
    print('Total de candidatos cadastrados: ',len(candidatos))


def modificar_nome(candidatos):
    nome_modificar = input('Nome do candidato que deseja modificar: ')
    nome = input('Novo nome: ')
    for i in range(len(candidatos)):
        if nome_modificar == candidatos[i][0]:
            candidatos[i][0] = nome


def modificar_partido(candidatos):
    nome = input('Nome do candidato: ')
    partido = input('Novo partido: ')
    for i in range(len(candidatos)):
        if nome == candidatos[i][0]:
            candidatos[i][3] = partido


def buscar_por_partido(candidatos):
    listar_candidatos(candidatos)
    partido = input('Digite o nome do partido que deseja fazer a buscar: ')
    print('Nome de todos os candidatos que são do partido {}!'.format(partido))
    for i in range(len(candidatos)):
        if partido == candidatos[i][3]:
            print(candidatos[i][0])


def menuzinho():
    menu = '1 - Modificar o nome\n' \
           '2 - Modificar o partido\n' \
           'opcao: '
    return int(input(menu))


def menu_principal():
    menu = '\n1 - Listar os candidatos cadastrados!!\n' \
           '2 - Adicionar um novo candidato!!\n' \
           '3 - Modificar informação de candidato!!\n' \
           '4 - Buscar todos os candidatos do mesmo partido!\n' \
           '0 - Sair\n' \
           'Opcao: '

    return int(input(menu))


def abrir_arquivo(nome_arquivo):
    matriz = cria_matriz(0, 6)
    fin = open(nome_arquivo)
    linha = fin.readlines()
    fin.close()
    for i in range(len(linha)):
        candidato = linha[i].strip().split('*')
        matriz.append(candidato)
    return matriz


def salvar_arquivo(nome_arquivo, candidatos_carregados):
    fout = open(nome_arquivo, 'w')
    for i in range(len(candidatos_carregados)):
        linha = '%s*%s*%s*%s*%s*%s\n' % (candidatos_carregados[i][0], candidatos_carregados[i][1],
                                    candidatos_carregados[i][2], candidatos_carregados[i][3],
                                    candidatos_carregados[i][4], candidatos_carregados[i][5])
        fout.write(linha)
    fout.close()


main()