from utils_matrizes import *

def main():
    dados = []

    carregar('enem2014_nota_por_escola.txt.csv')
    abrir(dados)
    opcao = menu_principal()
    while opcao != 0:
        if opcao == 1:
            listar_dados(dados)

        elif opcao == 2:
            top_geral(dados)

        elif opcao == 3:
            opcao1 = menuzinho1()
            if opcao1 == 1:
                tops(dados, 'matematica')
            elif opcao1 == 2:
                tops(dados, 'linguagens')
            elif opcao1 == 3:
                tops(dados, 'ciencias_natureza')
            elif opcao1 == 4:
                tops(dados, 'humanas')
            elif opcao1 == 5:
                tops(dados, 'redacao')

        elif opcao == 4:
            top_estado(dados)

        elif opcao == 5:
            top_estado_e_rede(dados)

        elif opcao == 6:
            opcao2 = menuzinho2()
            if opcao2 == 1:
                media(dados, 'matematica')
            elif opcao2 == 2:
                media(dados, 'linguagens')
            elif opcao2 == 3:
                media(dados, 'ciencias_natureza')
            elif opcao2 == 4:
                media(dados, 'redacao')
            elif opcao2 == 5:
                media(dados, 'humanas')

        elif opcao == 7:
            area = input('Digite a área: ')
            top_escola_e_estado_e_area(dados, area)

        elif opcao == 8:
            buscar_por_parte_nome(dados)

        elif opcao == 9:
            nota = float(input('Digite a nota: '))
            estado = input('Digite o estado: ')
            ranking_acima(dados, nota, estado)
            ranking_abaixo(dados, nota, estado)

        elif opcao == 10:
            opcao3 = menuzinho3()
            if opcao3 == 1:
                ranking(dados, 'nordeste')
            elif opcao3 == 2:
                ranking(dados, 'norte')
            elif opcao3 == 3:
                ranking(dados, 'centro')
            elif opcao3 == 4:
                ranking(dados, 'sudeste')
            elif opcao3 == 5:
                ranking(dados, 'sul')

        elif opcao == 0:
            break

        opcao = menu_principal()


def top_estado(dados):
    entrada = input('Digite o estado: ')
    lista = []
    for i in range(len(dados)):
        if entrada == dados[i]['uf']:
            lista.append(dados[i])
            if len(lista) > 20:
                break
    bubble(lista, 'media_objetivas', True)
    for j in range(0, 20):
        print('Estado: %s\n'
              'Escola: %s\n'
              'Posicao: %s\n'
              'Nota: %s\n' % (lista[j]['uf'], lista[j]['nome'], j, lista[j]['media_objetivas']))
    print('Os tops 20 do estado do {}'.format(entrada))


def top_estado_e_rede(dados):
    estado = input('Digite o estado: ')
    rede = input('Digite a rede: ')
    lista = []
    for i in range(len(dados)):
        if estado == dados[i]['uf'] and rede == dados[i]['rede']:
            lista.append(dados[i])
            if len(lista) > 20:
                break
    bubble(lista, 'media_objetivas', True)
    for j in range(0, 20):
        print('Estado: %s\n'
              'Escola: %s\n'
              'Rede: %s\n'
              'Posicao: %s\n'
              'Nota: %s\n' % (lista[j]['uf'], lista[j]['nome'], lista[j]['rede'], j, lista[j]['media_objetivas']))
    print('Os tops 20 do estado do {} da rede {}'.format(estado, rede))


def top_escola_e_estado_e_area(dados, atributo):
    estado = input('Digite o estado: ')
    area = input('Digite a área: ')
    lista = []
    for i in range(len(dados)):
        if estado == dados[i]['uf'] and area == atributo:
            lista.append(dados[i])
            if len(lista) > 5:
                break
    bubble(lista, atributo, True)
    for j in range(len(lista)):
        print('Estado: %s\n'
              'Escola: %s\n'
              'Rede: %s\n'
              'Posicao: %s\n'
              'Nota na área: %s\n' % (lista[j]['uf'], lista[j]['nome'], lista[j]['rede'], j, lista[j][area]))
    print('As tops 6 escolas do {} da área {}'.format(estado, area))


def tops(dados, atributo):
    bubble(dados, atributo, True)
    for j in range(0, 21):
        print('Escola: %s\n'
              'Posicao na área: %s\n'
              'Nota na área de %s: %s\n' % (dados[j]['nome'], j, atributo, dados[j][atributo]))


def media(dados, atributo):
    bubble(dados, atributo, True)
    soma, contador = 0, 0
    for i in range(len(dados)):
        if dados[i][atributo]:
            soma += dados[i][atributo]
            contador += 1
    print('Media nacional na área de {}: {:.2f}'.format(atributo, (soma/contador)))


def top_geral(dados):
    print('Estes são as 21 escolas com melhores médias!!')
    bubble(dados, 'media_objetivas', True)
    for j in range(0, 21):
        print('Escola: %s\n'
              'Posicao GERAL: %s\n'
              'Média geral da escola: %s\n' % (dados[j]['nome'], j, dados[j]['media_objetivas']))


def ranking(dados, regiao):
    lista = []
    for i in range(len(dados)):
        if regiao == 'nordeste':
            if dados[i]['uf'] == 'MA' or dados[i]['uf'] == 'PI' or \
                dados[i]['uf'] == 'AL' or dados[i]['uf'] == 'BH' or \
                dados[i]['uf'] == 'CE' or dados[i]['uf'] == 'PB' or \
                dados[i]['uf'] == 'PE' or dados[i]['uf'] == 'RN' or dados[i]['uf'] == 'SE':
                lista.append(dados[i])

        elif regiao == 'norte':
            if dados[i]['uf'] == 'AC' or dados[i]['uf'] == 'AP' or \
                dados[i]['uf'] == 'PA' or dados[i]['uf'] == 'AM' or \
                dados[i]['uf'] == 'RO' or dados[i]['uf'] == 'TO' or \
                dados[i]['uf'] == 'RR':
                lista.append(dados[i])

        elif regiao == 'centro':
            if dados[i]['uf'] == 'DF' or dados[i]['uf'] == 'GO' or \
                dados[i]['uf'] == 'MT' or dados[i]['uf'] == 'MS':
                lista.append(dados[i])

        elif regiao == 'sudeste':
            if dados[i]['uf'] == 'ES' or dados[i]['uf'] == 'MG' or \
                dados[i]['uf'] == 'RJ' or dados[i]['uf'] == 'SP':
                lista.append(dados[i])

        elif regiao == 'sul':
            if dados[i]['uf'] == 'PR' or dados[i]['uf'] == 'SC' or dados[i]['uf'] == 'RS':
                lista.append(dados[i])
    bubble(lista, 'media_objetivas', True)

    print('Região: %s'%regiao)
    for j in range(len(lista)):
        print('\nEstado: %s'%lista[j]['uf'])
        print('Municipio: %s'%lista[j]['municipio'])
        print('Escola: %s'%lista[j]['nome'])
        print('Posição: %d'%j)
        print('Nota: %s\n'%lista[j]['media_objetivas'])

def ranking_acima(dados, nota, estado):
    print('Este ranking é com base na nota média {}'.format(nota))
    for i in range(len(dados)):
        if estado == dados[i]['uf']:
            if dados[i]['media_objetivas'] >= nota:
                print('Escola: %s\n'
                      'Nota: %s\n'%(dados[i]['nome'], dados[i]['media_objetivas']))
    print('Estas são as escolas com notas acima da nota %d\n'%nota)


def ranking_abaixo(dados, nota, estado):
    print('Este ranking é com base na nota média {}'.format(nota))
    for i in range(len(dados)):
        if estado == dados[i]['uf']:
            if dados[i]['media_objetivas'] <= nota:
                print('Escola: %s\n'
                      'Nota: %s\n' % (dados[i]['nome'], dados[i]['media_objetivas']))
    print('Estas são as escolas com notas abaixo da nota %d\n' % nota)


def listar_dados(dados):
    for i in dados:
        print(i)

def buscar_por_parte_nome(dados):
    estado = input('Digite o seu estado: ')
    busca = input('Digite parte do nome da escola: ')
    contador = 0
    for i in range(len(dados)):
        if dados[i]['uf'] == estado and busca in dados[i]['nome']:
            contador += 1
            print('\n',dados[i]['nome'])
    print('{} Escola(s) encontradas'.format(contador))


def carregar(nome_arquivo):
    arquivo = open(nome_arquivo)
    linha = arquivo.readlines()
    lista = []
    for i in range(len(linha)):
        linhas = linha[i].replace(',', '.').strip().split(';')
        lista.append(linhas)
    return lista


def abrir(lista):
    dados = carregar('enem2014_nota_por_escola.txt.csv')
    for i in range(len(dados)):
        x = dic(dados[i])
        lista.append(x)
    print('Os dados das {} escolas foram carregados!'.format(len(lista)))


def menuzinho1():
    print('Qualquer uma das opções abaixo mostrará apenas os 20 primeiros!!')
    menu = '\n1 - Matematica\n' \
           '2 - Linguagens\n' \
           '3 - Ciencias da natureza\n' \
           '4 - Humanas\n' \
           '5 - Redação\n' \
           'opcao: '
    return int(input(menu))


def menu_principal():
    print('----ENEM----')
    menu = "\n1 - Listar dados\n" \
           "2 - Top geral\n" \
           "3 - Tops escolas por área\n" \
           "4 - Tops escolas por estado\n" \
           "5 - Tops escolas de cada estado por rede\n" \
           "6 - Médias Nacional por área\n" \
           "7 - Top escola por área e estado\n" \
           "8 - Buscar por nome\n" \
           "9 - Ranking por estado\n" \
           "10 - Ranking por região\n" \
           "0 - Sair\n" \
           "Opcao: "
    return int(input(menu))


def menuzinho2():
    print('Selecione uma opção abaixo!')
    menu = '\n1 - Média matemática\n' \
           '2 - Média linguagens\n' \
           '3 - Média ciências da natureza\n' \
           '4 - Média redação\n' \
           '5 - Média humanas\n' \
           'Opcao: '
    return int(input(menu))


def menuzinho3():
    menu = '1 - Nordeste\n' \
           '2 - Norte\n' \
           '3 - Centro\n' \
           '4 - Sudeste\n' \
           '5 - Sul\n' \
           'opcao: '
    return int(input(menu))

def dic(lista):
    dicionario = {}
    for i in range(len(lista)):
        dicionario['ranking'] = lista[0]
        dicionario['nome'] = lista[1]
        dicionario['municipio'] = lista[2]
        dicionario['uf'] = lista[3]
        dicionario['rede'] = lista[4]
        dicionario['permanencia'] = lista[5]
        dicionario['nivel_socio_economico'] = lista[6]
        dicionario['media_objetivas'] = float(lista[7])
        dicionario['linguagens'] = float(lista[8])
        dicionario['matematica'] = float(lista[9])
        dicionario['ciencias_natureza'] = float(lista[10])
        dicionario['humanas'] = float(lista[11])
        dicionario['redacao'] = float(lista[12])
    return dicionario


def bubble(colecao, atributo, inverso):
    for i in range(len(colecao)):
        for j in range(len(colecao)-i-1):
            if inverso:
                if colecao[j][atributo] < colecao[j+1][atributo]:
                    x = colecao[j]
                    colecao[j] = colecao[j+1]
                    colecao[j+1] = x
            else:
                if colecao[j][atributo] > colecao[j+1][atributo]:
                    x = colecao[j]
                    colecao[j] = colecao[j+1]
                    colecao[j+1] = x

main()