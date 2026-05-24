def main():
    texto = input('texto: ')
    caractere = input('Caractere: ')
    quantidade = quantidade_caractere(texto, caractere)
    
    print(f'''
    >>> Resumo <<<
    Caractere desejado: {caractere}
    Quantidade dele no texto: {quantidade}
    ''')
    
def quantidade_caractere(texto, caractere):
    contador = 0
    for i in texto:
        if i == caractere:
            contador += 1
            
    return contador
        
        
main()