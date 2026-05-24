def main():
    nome = input('Nome completo: ')
    nome_sobrenome(nome)
    
def nome_sobrenome(nome):
    novo_nome = nome.split(' ')
    
    print(f'{novo_nome[-1]} / {novo_nome[0]}')
main()