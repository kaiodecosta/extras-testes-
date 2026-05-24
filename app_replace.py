def main():
    texto = input('Texto: ')
    letra = input('Letra: ')
    substituto = input('Substituto: ')
    
    novo_texto = Replace(texto, letra, substituto)
    
    print(novo_texto)
    
def Replace(texto, letra, substituto):
    novo_texto = ''
    for caractere in texto:
        if caractere == letra:
            novo_texto += substituto
        else:
            novo_texto += caractere
    return novo_texto

main()