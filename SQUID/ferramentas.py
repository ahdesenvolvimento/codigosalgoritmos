def show_afonso(lista):
    for i in lista:
        print(i)

def arquivo():
    arquivo = open('access.log', 'r')
    lista = []
    for linha in arquivo:
        linha2 = linha.strip().split() #strip é para quebrar o espaço e o split é para criar os indices
        lista.append(linha2)

    return lista

def site_por_ip(lista):
    ip = input('Digite o IP desejado: ')
    lista1 = []
    contador = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][2] == ip:
                if lista[i][6] not in lista1:
                    lista1.append(lista[i][6])
                    print(lista[i][6])
                    contador += 1
    print('O numero de sites acessados por este IP foi %d'%contador)

def total_bytes_por_ip(lista):
    ip = input('Digite o IP desejado: ')
    lista1 = []
    soma = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][2] == ip:
                if lista[i][4] not in lista1:
                    lista1.append(lista[i][4])
                    soma += int(lista[i][4])
    print('O numero total de Bytes por este IP foi %d' % soma)



def soma_todos_bytes(lista):
    soma = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][4]:
                soma += int(lista[i][4])
    print('A soma total de Bytes é %d'%soma)

def todos_clientes(lista):
    lista1 = []
    dic = {}
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][2] not in lista1:
                lista1.append(lista[i][2])
    x = criar_dic(lista1)


def criar_dic(lista): #cada elemento da lista tem que ser único.
    d = dict()
    lista1 = []
    for i in lista:
        d[i] = []
    lista1.append(d)

    return lista1

def acesso_site(lista):
    contador = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if 'TCP_MISS' in lista[i][3]:
                contador += 1
    print(contador/100000)