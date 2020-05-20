from ferramentas import *
lista = arquivo()
def main():
    while True:
                #Questão 1
        menu =  '1 - Numero de sites diferentes acessados por cada cliente IP\n' \
                '2 - Listar acesso de um determinado cliente\n' \
                '3 - Numero em Bytes de dados\n' \
                '4 - Listar total de bytes por IP\n' \
                '5 - Percentual de sites encontrados na cache e de sites trazidos diretamente da internet'
                #Questão 2

        opcao = int(input(menu))

        if opcao == 1:
            todos_clientes(lista)
        if opcao == 2:
            site_por_ip(lista)
        if opcao == 3:
            soma_todos_bytes(lista)
        if opcao == 4:
            total_bytes_por_ip(lista)
        if opcao == 5:
            acesso_site(lista)
            
if __name__ == '__main__':
    main()