from fun_io import obter_dado, escrever

def main():
    idade = int(obter_dado('qual sua idade?: '))
    adulto = se_adulto(idade)
    escrever(f'Você tem {idade} anos, {adulto}')
    

def se_adulto(numero):
    if numero > 17:
        return 'Olá Adulto!!'
    else: 
        return 'Tchau'


main()